from django.contrib import admin

from .models import Subject, Course, Module


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """
    Административный интерфейс модели 'Предмет' (Subject)
    Настройки включают:
    - Отображение полей 'Название' (title), slug
    - Параметр для автоматического заполнения slug на основе 'Название' (title)
    """

    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
    """
    Административный интерфейс модели 'Модуль' (Module)
    Настройки включают:
    - вложенное редактирование модели 'Модуль' на страничке модели 'Курс' 
    """

    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Административный интерфейс модели 'Курс' (Course)
    Настройки включают:
    - Отображение полей 'Название' (title), 'Предмет' (subject), 'Дата создания' (created)
    - Фильтрация по полям 'Дата создания' (created) и 'Предмет' (subject)
    - Поля поиска по полям 'Название' (title), 'Описание' (overview)
    - Параметр для автоматического заполнения slug на основе 'Название' (title)
    """

    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]