# Education Project

Django проект для образовательной платформы.

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-логин/education.git
cd education
Создайте виртуальное окружение и активируйте его:

bash
python -m venv venv
# Для Windows: venv\Scripts\activate
# Для Linux/Mac: source venv/bin/activate
Установите зависимости:

bash
pip install -r requirements.txt
Настройте переменные окружения:

bash
cp .env.example .env
# Отредактируйте .env файл
Примените миграции:

bash
python manage.py migrate
Создайте суперпользователя:

bash
python manage.py createsuperuser
Запустите сервер:

bash
python manage.py runserver
Структура проекта
education/ — основные настройки проекта

courses/ — приложение курсов

students/ — приложение студентов

media/ — медиафайлы

text

2. **.gitkeep для media** (чтобы сохранить структуру):
```bash
# Создайте пустой файл, чтобы папка media сохранилась в Git
touch media/.gitkeep