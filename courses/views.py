from django.shortcuts import redirect, get_object_or_404
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import TemplateResponseMixin, View
from django.forms.models import modelform_factory
from django.apps import apps
from django.db.models import Count
from django.views.generic.detail import DetailView
from django.contrib import messages

from .forms import ModuleFormSet, GradeForm, AnswerForm
from .models import Course, Module, Content, Subject, Answer
from students.forms import CourseEnrollForm


class OwnerMixin(object):
    """
    Миксин, переопределяет метод get_queryset
    - формирует объекты только текущего пользователя
    """

    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin(object):
    """
    Миксин, переопределяет метод form_valid
    - назначает текущего пользователя владельцем создаваемого/редактируемого объекта
    """

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)
    

class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin):
    """
    Миксин, устанавливает модель
    """
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')

class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    """
    Миксин
    - Устанавливает поля модели в которых будут изменяться или создаваться данные
    - Перенаправляет на страницу-шаблон в случае успешных действий 
    - Определяет шаблон
    """
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')
    template_name = 'courses/manage/course/form.html'


class ManageCourseListView(OwnerCourseMixin, ListView):
    """
    Создает список курсов отфильтрованых по пользователю
    - Использует модель Course
    - Использует шаблон courses/manage/course/list.html
    """

    template_name = 'courses/manage/course/list.html'

    
class CourseCreateView(PermissionRequiredMixin, OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'


class CourseUpdateView(PermissionRequiredMixin, OwnerCourseEditMixin, UpdateView):
    permission_required = 'courses.change_course'


class CourseDeleteView(PermissionRequiredMixin, OwnerCourseMixin, DeleteView):
    """
    
    """
    permission_required = 'courses.delete_course'
    template_name = 'courses/manage/course/delete.html'
    success_url = reverse_lazy('manage_course_list')


class CourseModuleUpdateView(TemplateResponseMixin, View):
    """
    FormSet для отображения модулей в курсах
    - вызывает шаблон formset.html
    - формирует FormSet
    - находит курс по pk и проверяет, что владелец - текущий пользователь, маршрутизирует между get и post
    - обрабатывает get запрос
    - обрабатывает post запрос
    Порядок выполнения:
    GET:
        dispatch() → get() → get_formset() → render_to_response()
    POST:
        dispatch() → post() → get_formset(data=POST) → is_valid() → save() → redirect()
    """

    template_name = 'courses/manage/module/formset.html'
    course = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course, data=data)
    
    def dispatch(self, request, pk):
        self.course = get_object_or_404(Course, id=pk, owner=request.user)
        return super(CourseModuleUpdateView, self).dispatch(request, pk)
    
    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'course': self.course, 'formset': formset})
    
    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save(commit=True)
            return redirect('manage_course_list')
        return self.render_to_response({'course': self.course, 'formset': formset})


class ContentCreateUpdateView(TemplateResponseMixin, View):
    """
    Управление содержимым модулей
    - вызывает шаблон form.html
    - возвращает модель по имени
    - создает форму по указанным полям
    - обрабатывает get запрос
    - обрабатывает post запрос
    - перенаправляет по указанному URL
    """

    module = None
    model = None
    obj = None
    template_name = 'courses/manage/content/form.html'

    def get_model(self, model_name):
        if model_name in ['text', 'video', 'image', 'file']:
            return apps.get_model(app_label='courses', model_name=model_name)
        return None

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['owner',
                                                 'title',
                                                 'order',
                                                 'created',
                                                 'updated'])
        return Form(*args, **kwargs)

    def dispatch(self, request, module_id, model_name, id=None):
        self.module = get_object_or_404(Module, id=module_id, course__owner=request.user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model, id=id, owner=request.user)
        return super(ContentCreateUpdateView, self).dispatch(request, module_id, model_name, id)

    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({'form': form, 'object': self.obj})

    def post(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj, data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            if not id:
                Content.objects.create(module=self.module, item=obj)
            return redirect('module_content_list', self.module.id)
        return self.render_to_response({'form': form, 'object': self.obj})


class ContentDeleteView(View):
    """
    Удаление содержимого модуля
    - Удаляет запись модуля (контент)
    - перенаправляет по указанному URL
    """

    def post(self, request, id):
        content = get_object_or_404(Content, id=id, module__course__owner=request.user)
        module = content.module
        content.item.delete()
        content.delete()
        return redirect('module_content_list', module.id)


class ModuleContentListView(TemplateResponseMixin, View):
    """
    Отображение содержимого модуля
    """
    template_name = 'courses/manage/module/content_list.html'

    def get(self, request, id):
        module = get_object_or_404(Module,
                                 id=id,
                                 course__owner=request.user)
        return self.render_to_response({'module': module})
    

class CourseListView(TemplateResponseMixin, View):
    """
    Формирует список курсов в предметах
    - создает QuerySet из моделей Subject и Course
    - устанавливает фильтр на курс
    """
    model = Course
    template_name = 'courses/course/list.html'

    def get(self, request, subject=None): 
        subjects = Subject.objects.annotate(total_courses=Count('courses'))
        courses = Course.objects.annotate(total_modules=Count('modules'))
        if subject:
            subject = get_object_or_404(Subject, slug=subject)
            courses = courses.filter(subject=subject)
        return self.render_to_response({'subjects': subjects, 'subject': subject, 'courses': courses})
    

class CourseDetailView(DetailView):
    """
    Формирует данные для странички курса
    - Используемая модель
    - Название шаблона
    - Добавляет форму для записи на курс в контекст детального представления курса.
    """
    model = Course
    template_name = 'courses/course/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['enroll_form'] = CourseEnrollForm(initial={'course':self.object})
        return context
    


def custom_login_redirect(request):
    if request.user.groups.filter(name='Teachers').exists():
        return redirect('manage_course_list')
    else:
        return redirect('course_list')
    

class AnswersListView(LoginRequiredMixin, ListView):
    """
    Представление для списка всех ответов
    1. Собирает queryset по тем курсам, принадлежащим данному пользователю-учителю
    """
    model = Answer
    template_name = 'courses/manage/module/answers_list.html'
    context_object_name = 'answers'
    
    def get_queryset(self):
        teacher_courses = Course.objects.filter(owner=self.request.user)
        return Answer.objects.filter(module__course__in=teacher_courses).select_related('student', 'module')


class AnswerDetailView(LoginRequiredMixin, UpdateView):
    """
    Представление для просмотра и оценки ответа
    1. Вызывает заранее сделанную форму, после заполнения которой перенаправляет на страницу с перечисленными ответами
    """
    model = Answer
    form_class = GradeForm
    template_name = 'courses/manage/module/view_answer.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Оценка сохранена!')
        return reverse_lazy('answers_list')


class AnswerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Представление для удаления ответа
    1. Удаляет ответ в базе Answer
    """
    model = Answer
    success_url = reverse_lazy('answers_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Ответ успешно удален!')
        return super().delete(request, *args, **kwargs)


class AnswerCreateView(LoginRequiredMixin, CreateView):
    """
    Представление для создания ответа (прикрепления файла)
    1. Если форма валидна, то присвает значениям полей моделей нынешнего пользователя, прикрепленный файл и модуль
    2. Перенаправляет обратно на страницу с модулем
    """
    model = Answer
    form_class = AnswerForm
    template_name = 'courses/manage/module/answer_form.html'
    
    def form_valid(self, form):
        module = get_object_or_404(Module, id=self.kwargs['module_id'])
        form.instance.student = self.request.user
        form.instance.module = module
        messages.success(self.request, 'Файл успешно прикреплен!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('student_course_detail_module', 
                          args=[self.object.module.course.id, self.object.module.id])
