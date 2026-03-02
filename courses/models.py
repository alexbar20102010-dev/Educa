from django.db import models
from .fields import OrderField

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string

from django.contrib.contenttypes.fields import GenericForeignKey


class Subject(models.Model):
    """Модель предмета обучения"""

    title = models.CharField(max_length=200, verbose_name='Название предмета')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Предметы'
        verbose_name = 'Предмет'

    def __str__(self):
        return self.title
        

class Course(models.Model):
    """Модель курса в предмете обучения"""

    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE, verbose_name='Предмет')
    title = models.CharField(max_length=200, verbose_name='Название курса')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL (на английском)')
    overview = models.TextField(verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    students = models.ManyToManyField(User, related_name='courses_joined', blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'

    def __str__(self):
        return self.title
        

class Module(models.Model):
    """Модель модуля в курсе предмета обучения"""

    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Название модуля')
    description = models.TextField(blank=True, verbose_name='Описание модуля')
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        verbose_name_plural = 'Модули'
        verbose_name = 'Модуль'
        ordering = ['order']

    def __str__(self):
        return self.title

class Content(models.Model):
    """
    Модель контента.
    Реализованна обобщающая связь объекта типа Content c любой другой моделью,
    представляющей тип содержимого. Чтобы обобщенные связи 
    работали, необходимо создать три поля в модели:
    - content_type - внешний ключ, ForeignKey, на модель ContentType;
    - object_id - идентификатор связанного объекта типа PositiveIntegerField;
    - item - поле типа GenericForeignKey, которое обобщает данные из предыдущих двух
    """

    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                      limit_choices_to={'model__in':
                                                        ('text',
                                                         'video',
                                                         'image',
                                                         'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        verbose_name = 'Контент'
        ordering = ['order']


class ItemBase(models.Model):
    """
    Абстрактная модель, содержащая поля:
    - owner - данные пользователя, который создал контент
    - title - название контента
    - created - дата создания контента
    - updated - дата обновления контента
    """

    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE) #related_name='%(class)s_related' — это шаблон для динамического создания имен обратных связей в абстрактных моделях.
    title = models.TextField(verbose_name='Название контента')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания контента')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления контента')

    def render(self):
        return render_to_string('courses/content/{}.html'.format(self._meta.model_name), {'item': self})

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
    

class Text(ItemBase):
    """Наследуемая модель c текстом"""

    content = models.TextField(verbose_name='Текст')

    class Meta():
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'
    

class File(ItemBase):
    """Наследуемая модель c файлом"""
    
    file = models.FileField(upload_to='files', verbose_name='Файл')

    class Meta():
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class Image(ItemBase):
    """Наследуемая модель c картинкой"""
    
    file = models.FileField(upload_to='images', verbose_name='Картинка')

    class Meta():
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

class Video(ItemBase):
    """Наследуемая модель c видео"""
    
    url = models.URLField(verbose_name='Видео') #поле URLField сохраняет URL видео для его скачивания

    class Meta():
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Answer(models.Model):
    """Модель для хранения ответов проходящих курс"""

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers', verbose_name='Ученик')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='answers', verbose_name='Модуль')
    file = models.FileField(upload_to='answers/%Y/%m/%d/', verbose_name='Прикрепленный файл')
    grade = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, blank=True, verbose_name='Оценка')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
    
    def __str__(self):
        return f'{self.student.username} - {self.module.title}'