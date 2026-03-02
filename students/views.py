from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from courses.models import Answer, Module, Course
from .forms import CourseEnrollForm
from courses.forms import AnswerForm, GradeForm


class StudentRegistrationView(CreateView):
    """
    Класс регистрации студентов
    - Определяет шаблон
    - Определяет форму регистрации
    - Определяет страницу перенаправления
    - Создает учетную запись (родительский метод), Аутентифицирует нового пользователя, Выполняет автоматический вход после регистрации
    """
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super(StudentRegistrationView, self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        login(self.request, user)
        return result
    

class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    """
    Запись студента на курс
    - Атрибут который хранит курс
    - Используемая форма (определена в классе .forms.CourseEnrollForm)
    - Обработчик формы: из валидной формы извлекается выбранный курc, 
      текущий пользователь добавляется в отношение students курса, 
      вызывается родительский метод для завершения обработки
    - Метод перенаправления в случае успешной обработки
    """
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super(StudentEnrollCourseView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])


class StudentCourseListView(LoginRequiredMixin, ListView):
    """
    Отображение списка курсов, на которые записан студент
    - Используемая модель
    - Используемый шаблон
    - Получаем все курсы, фильтруем курсы, где текущий пользователь зарегистрирован на курс
    """
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super(StudentCourseListView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])
    

class StudentCourseDetailView(DetailView):
    """
    Отображение курса студента
    - Используемая модель
    - Используемый шаблон
    - Получаем все курсы, фильтруем курсы, где текущий пользователь зарегистрирован на курс
    - Метод добавляет в контекст текущий модуль курса для отображения в детальном представлении курса студента
      если модуль есть, то получаем текущий модуль
      если нет, то получаем первый модуль
    """
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super(StudentCourseDetailView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])
    
    def get_context_data(self, **kwargs):
        context = super(StudentCourseDetailView, self).get_context_data(**kwargs)
        course = self.get_object()
        if 'module_id' in self.kwargs:
            context['module'] = course.modules.get(id=self.kwargs['module_id'])
            return context
        elif 'module_id' not in self.kwargs:
            return context
        else:
            context['module'] = course.modules.all()[0]
            return context

