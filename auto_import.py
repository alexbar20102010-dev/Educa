# auto_import.py - запустить на Render
import os, django, json, sys
from pathlib import Path

# Настройка Django
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "education.settings")

try:
    django.setup()
except Exception as e:
    print(f"Ошибка настройки Django: {e}")
    sys.exit(1)

from django.apps import apps
from django.db import transaction

def import_data():
    print("🚀 Начинаем импорт данных на Render...")
    
    # Данные для импорта
    data = {
  "django_migrations": [
    {
      "id": 1,
      "app": "contenttypes",
      "name": "0001_initial",
      "applied": "2025-09-26 13:53:22.744559"
    },
    {
      "id": 2,
      "app": "auth",
      "name": "0001_initial",
      "applied": "2025-09-26 13:53:22.765502"
    },
    {
      "id": 3,
      "app": "admin",
      "name": "0001_initial",
      "applied": "2025-09-26 13:53:22.787135"
    },
    {
      "id": 4,
      "app": "admin",
      "name": "0002_logentry_remove_auto_add",
      "applied": "2025-09-26 13:53:22.807080"
    },
    {
      "id": 5,
      "app": "admin",
      "name": "0003_logentry_add_action_flag_choices",
      "applied": "2025-09-26 13:53:22.819797"
    },
    {
      "id": 6,
      "app": "contenttypes",
      "name": "0002_remove_content_type_name",
      "applied": "2025-09-26 13:53:22.845385"
    },
    {
      "id": 7,
      "app": "auth",
      "name": "0002_alter_permission_name_max_length",
      "applied": "2025-09-26 13:53:22.857883"
    },
    {
      "id": 8,
      "app": "auth",
      "name": "0003_alter_user_email_max_length",
      "applied": "2025-09-26 13:53:22.873214"
    },
    {
      "id": 9,
      "app": "auth",
      "name": "0004_alter_user_username_opts",
      "applied": "2025-09-26 13:53:22.886560"
    },
    {
      "id": 10,
      "app": "auth",
      "name": "0005_alter_user_last_login_null",
      "applied": "2025-09-26 13:53:22.897480"
    },
    {
      "id": 11,
      "app": "auth",
      "name": "0006_require_contenttypes_0002",
      "applied": "2025-09-26 13:53:22.904495"
    },
    {
      "id": 12,
      "app": "auth",
      "name": "0007_alter_validators_add_error_messages",
      "applied": "2025-09-26 13:53:22.916247"
    },
    {
      "id": 13,
      "app": "auth",
      "name": "0008_alter_user_username_max_length",
      "applied": "2025-09-26 13:53:22.933298"
    },
    {
      "id": 14,
      "app": "auth",
      "name": "0009_alter_user_last_name_max_length",
      "applied": "2025-09-26 13:53:22.945810"
    },
    {
      "id": 15,
      "app": "auth",
      "name": "0010_alter_group_name_max_length",
      "applied": "2025-09-26 13:53:22.960370"
    },
    {
      "id": 16,
      "app": "auth",
      "name": "0011_update_proxy_permissions",
      "applied": "2025-09-26 13:53:22.968946"
    },
    {
      "id": 17,
      "app": "auth",
      "name": "0012_alter_user_first_name_max_length",
      "applied": "2025-09-26 13:53:22.981964"
    },
    {
      "id": 18,
      "app": "courses",
      "name": "0001_initial",
      "applied": "2025-09-26 13:53:23.003281"
    },
    {
      "id": 19,
      "app": "sessions",
      "name": "0001_initial",
      "applied": "2025-09-26 13:53:23.015358"
    },
    {
      "id": 20,
      "app": "courses",
      "name": "0002_content_file_image_text_video",
      "applied": "2025-09-27 15:25:44.157211"
    },
    {
      "id": 21,
      "app": "courses",
      "name": "0003_alter_content_options_alter_module_options_and_more",
      "applied": "2025-09-29 15:21:11.155582"
    },
    {
      "id": 22,
      "app": "courses",
      "name": "0004_course_students_alter_course_subject",
      "applied": "2025-11-12 11:33:57.010201"
    }
  ],
  "auth_group_permissions": [
    {
      "id": 1,
      "group_id": 1,
      "permission_id": 5
    },
    {
      "id": 2,
      "group_id": 1,
      "permission_id": 6
    },
    {
      "id": 3,
      "group_id": 1,
      "permission_id": 7
    },
    {
      "id": 4,
      "group_id": 1,
      "permission_id": 8
    },
    {
      "id": 5,
      "group_id": 1,
      "permission_id": 9
    },
    {
      "id": 6,
      "group_id": 1,
      "permission_id": 10
    },
    {
      "id": 7,
      "group_id": 1,
      "permission_id": 11
    },
    {
      "id": 8,
      "group_id": 1,
      "permission_id": 12
    },
    {
      "id": 9,
      "group_id": 1,
      "permission_id": 37
    },
    {
      "id": 10,
      "group_id": 1,
      "permission_id": 38
    },
    {
      "id": 11,
      "group_id": 1,
      "permission_id": 39
    },
    {
      "id": 12,
      "group_id": 1,
      "permission_id": 40
    },
    {
      "id": 13,
      "group_id": 1,
      "permission_id": 41
    },
    {
      "id": 14,
      "group_id": 1,
      "permission_id": 42
    },
    {
      "id": 15,
      "group_id": 1,
      "permission_id": 43
    },
    {
      "id": 16,
      "group_id": 1,
      "permission_id": 44
    },
    {
      "id": 17,
      "group_id": 1,
      "permission_id": 45
    },
    {
      "id": 18,
      "group_id": 1,
      "permission_id": 46
    },
    {
      "id": 19,
      "group_id": 1,
      "permission_id": 47
    },
    {
      "id": 20,
      "group_id": 1,
      "permission_id": 48
    },
    {
      "id": 21,
      "group_id": 1,
      "permission_id": 49
    },
    {
      "id": 22,
      "group_id": 1,
      "permission_id": 50
    },
    {
      "id": 23,
      "group_id": 1,
      "permission_id": 51
    },
    {
      "id": 24,
      "group_id": 1,
      "permission_id": 52
    },
    {
      "id": 25,
      "group_id": 1,
      "permission_id": 53
    },
    {
      "id": 26,
      "group_id": 1,
      "permission_id": 54
    },
    {
      "id": 27,
      "group_id": 1,
      "permission_id": 55
    },
    {
      "id": 28,
      "group_id": 1,
      "permission_id": 56
    }
  ],
  "auth_user_groups": [
    {
      "id": 3,
      "user_id": 5,
      "group_id": 1
    }
  ],
  "auth_user_user_permissions": [],
  "django_admin_log": [
    {
      "id": 1,
      "object_id": "1",
      "object_repr": "\u0424\u043b\u043e\u0440\u0438\u0441\u0442\u0438\u043a\u0430",
      "action_flag": 1,
      "change_message": "[{\"added\": {}}]",
      "content_type_id": 1,
      "user_id": 1,
      "action_time": "2025-09-29 15:27:41.960610"
    },
    {
      "id": 2,
      "object_id": "1",
      "object_repr": "\u0420\u043e\u0437\u044b",
      "action_flag": 1,
      "change_message": "[{\"added\": {}}, {\"added\": {\"name\": \"\\u041c\\u043e\\u0434\\u0443\\u043b\\u044c\", \"object\": \"\\u0411\\u0435\\u043b\\u044b\\u0435 \\u0440\\u043e\\u0437\\u044b\"}}, {\"added\": {\"name\": \"\\u041c\\u043e\\u0434\\u0443\\u043b\\u044c\", \"object\": \"\\u041a\\u0440\\u0430\\u0441\\u043d\\u044b\\u0435 \\u0440\\u043e\\u0437\\u044b\"}}, {\"added\": {\"name\": \"\\u041c\\u043e\\u0434\\u0443\\u043b\\u044c\", \"object\": \"\\u0416\\u0435\\u043b\\u0442\\u044b\\u0435 \\u0440\\u043e\\u0437\\u044b\"}}]",
      "content_type_id": 2,
      "user_id": 1,
      "action_time": "2025-09-29 15:29:45.534188"
    },
    {
      "id": 3,
      "object_id": "1",
      "object_repr": "Teachers",
      "action_flag": 1,
      "change_message": "[{\"added\": {}}]",
      "content_type_id": 6,
      "user_id": 1,
      "action_time": "2025-10-05 08:31:32.257064"
    },
    {
      "id": 4,
      "object_id": "2",
      "object_repr": "ivanov",
      "action_flag": 1,
      "change_message": "[{\"added\": {}}]",
      "content_type_id": 7,
      "user_id": 1,
      "action_time": "2025-10-05 08:36:18.998573"
    },
    {
      "id": 5,
      "object_id": "2",
      "object_repr": "ivanov",
      "action_flag": 2,
      "change_message": "[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Groups\"]}}]",
      "content_type_id": 7,
      "user_id": 1,
      "action_time": "2025-10-05 08:37:24.122249"
    },
    {
      "id": 6,
      "object_id": "3",
      "object_repr": "petrov",
      "action_flag": 1,
      "change_message": "[{\"added\": {}}]",
      "content_type_id": 7,
      "user_id": 1,
      "action_time": "2025-10-18 12:06:35.530832"
    },
    {
      "id": 7,
      "object_id": "3",
      "object_repr": "petrov",
      "action_flag": 2,
      "change_message": "[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Groups\"]}}]",
      "content_type_id": 7,
      "user_id": 1,
      "action_time": "2025-10-18 12:08:52.535000"
    },
    {
      "id": 8,
      "object_id": "4",
      "object_repr": "\u041c\u0430\u043a\u0438",
      "action_flag": 2,
      "change_message": "[{\"added\": {\"name\": \"\\u041c\\u043e\\u0434\\u0443\\u043b\\u044c\", \"object\": \"\\u041c\\u0430\\u043a\\u0438 \\u0441\\u0438\\u043d\\u0438\\u0435\"}}]",
      "content_type_id": 2,
      "user_id": 1,
      "action_time": "2025-10-18 12:36:14.238465"
    },
    {
      "id": 9,
      "object_id": "4",
      "object_repr": "\u041c\u0430\u043a\u0438",
      "action_flag": 2,
      "change_message": "[]",
      "content_type_id": 2,
      "user_id": 1,
      "action_time": "2025-10-18 12:51:27.473193"
    },
    {
      "id": 10,
      "object_id": "4",
      "object_repr": "\u041c\u0430\u043a\u0438",
      "action_flag": 2,
      "change_message": "[{\"changed\": {\"name\": \"\\u041c\\u043e\\u0434\\u0443\\u043b\\u044c\", \"object\": \"\\u041c\\u0430\\u043a\\u0438 \\u0436\\u0435\\u043b\\u0442\\u044b\\u0435\", \"fields\": [\"Order\"]}}, {\"changed\": {\"name\": \"\\u041c\\u043e\\u0434\\u0443\\u043b\\u044c\", \"object\": \"\\u041c\\u0430\\u043a\\u0438 \\u0441\\u0438\\u043d\\u0438\\u0435\", \"fields\": [\"Order\"]}}]",
      "content_type_id": 2,
      "user_id": 1,
      "action_time": "2025-10-18 13:21:28.608546"
    },
    {
      "id": 11,
      "object_id": "2",
      "object_repr": "\u0411\u0438\u043e\u043b\u043e\u0433\u0438\u044f",
      "action_flag": 1,
      "change_message": "[{\"added\": {}}]",
      "content_type_id": 1,
      "user_id": 1,
      "action_time": "2025-11-08 14:05:34.424242"
    },
    {
      "id": 12,
      "object_id": "2",
      "object_repr": "\u0411\u0438\u043e\u043b\u043e\u0433\u0438\u044f",
      "action_flag": 2,
      "change_message": "[]",
      "content_type_id": 1,
      "user_id": 1,
      "action_time": "2025-11-08 14:06:15.252932"
    },
    {
      "id": 13,
      "object_id": "1",
      "object_repr": "\u0420\u043e\u0437\u044b",
      "action_flag": 2,
      "change_message": "[{\"changed\": {\"fields\": [\"Owner\"]}}]",
      "content_type_id": 2,
      "user_id": 1,
      "action_time": "2025-11-14 12:41:32.318229"
    },
    {
      "id": 14,
      "object_id": "2",
      "object_repr": "ivanov",
      "action_flag": 3,
      "change_message": "",
      "content_type_id": 7,
      "user_id": 1,
      "action_time": "2025-12-23 09:06:39.807921"
    },
    {
      "id": 15,
      "object_id": "3",
      "object_repr": "petrov",
      "action_flag": 3,
      "change_message": "",
      "content_type_id": 7,
      "user_id": 1,
      "action_time": "2025-12-23 09:06:39.807921"
    },
    {
      "id": 16,
      "object_id": "4",
      "object_repr": "sidorov",
      "action_flag": 3,
      "change_message": "",
      "content_type_id": 7,
      "user_id": 1,
      "action_time": "2025-12-23 09:06:39.807921"
    },
    {
      "id": 17,
      "object_id": "5",
      "object_repr": "epstein",
      "action_flag": 1,
      "change_message": "[{\"added\": {}}]",
      "content_type_id": 7,
      "user_id": 1,
      "action_time": "2025-12-23 09:07:29.032715"
    },
    {
      "id": 18,
      "object_id": "2",
      "object_repr": "\u0411\u0438\u043e\u043b\u043e\u0433\u0438\u044f",
      "action_flag": 3,
      "change_message": "",
      "content_type_id": 1,
      "user_id": 1,
      "action_time": "2025-12-23 09:08:18.987503"
    },
    {
      "id": 19,
      "object_id": "1",
      "object_repr": "\u0424\u043b\u043e\u0440\u0438\u0441\u0442\u0438\u043a\u0430",
      "action_flag": 3,
      "change_message": "",
      "content_type_id": 1,
      "user_id": 1,
      "action_time": "2025-12-23 09:08:21.378483"
    },
    {
      "id": 20,
      "object_id": "3",
      "object_repr": "\u0412\u0435\u0440\u0441\u0442\u043a\u0430",
      "action_flag": 1,
      "change_message": "[{\"added\": {}}]",
      "content_type_id": 1,
      "user_id": 1,
      "action_time": "2025-12-23 09:08:31.615991"
    },
    {
      "id": 21,
      "object_id": "5",
      "object_repr": "epstein",
      "action_flag": 2,
      "change_message": "[{\"changed\": {\"fields\": [\"Groups\"]}}]",
      "content_type_id": 7,
      "user_id": 1,
      "action_time": "2025-12-23 09:08:52.606177"
    }
  ],
  "django_content_type": [
    {
      "id": 1,
      "app_label": "courses",
      "model": "subject"
    },
    {
      "id": 2,
      "app_label": "courses",
      "model": "course"
    },
    {
      "id": 3,
      "app_label": "courses",
      "model": "module"
    },
    {
      "id": 4,
      "app_label": "admin",
      "model": "logentry"
    },
    {
      "id": 5,
      "app_label": "auth",
      "model": "permission"
    },
    {
      "id": 6,
      "app_label": "auth",
      "model": "group"
    },
    {
      "id": 7,
      "app_label": "auth",
      "model": "user"
    },
    {
      "id": 8,
      "app_label": "contenttypes",
      "model": "contenttype"
    },
    {
      "id": 9,
      "app_label": "sessions",
      "model": "session"
    },
    {
      "id": 10,
      "app_label": "courses",
      "model": "image"
    },
    {
      "id": 11,
      "app_label": "courses",
      "model": "content"
    },
    {
      "id": 12,
      "app_label": "courses",
      "model": "video"
    },
    {
      "id": 13,
      "app_label": "courses",
      "model": "file"
    },
    {
      "id": 14,
      "app_label": "courses",
      "model": "text"
    }
  ],
  "auth_permission": [
    {
      "id": 1,
      "content_type_id": 1,
      "codename": "add_subject",
      "name": "Can add \u041f\u0440\u0435\u0434\u043c\u0435\u0442"
    },
    {
      "id": 2,
      "content_type_id": 1,
      "codename": "change_subject",
      "name": "Can change \u041f\u0440\u0435\u0434\u043c\u0435\u0442"
    },
    {
      "id": 3,
      "content_type_id": 1,
      "codename": "delete_subject",
      "name": "Can delete \u041f\u0440\u0435\u0434\u043c\u0435\u0442"
    },
    {
      "id": 4,
      "content_type_id": 1,
      "codename": "view_subject",
      "name": "Can view \u041f\u0440\u0435\u0434\u043c\u0435\u0442"
    },
    {
      "id": 5,
      "content_type_id": 2,
      "codename": "add_course",
      "name": "Can add \u041a\u0443\u0440\u0441"
    },
    {
      "id": 6,
      "content_type_id": 2,
      "codename": "change_course",
      "name": "Can change \u041a\u0443\u0440\u0441"
    },
    {
      "id": 7,
      "content_type_id": 2,
      "codename": "delete_course",
      "name": "Can delete \u041a\u0443\u0440\u0441"
    },
    {
      "id": 8,
      "content_type_id": 2,
      "codename": "view_course",
      "name": "Can view \u041a\u0443\u0440\u0441"
    },
    {
      "id": 9,
      "content_type_id": 3,
      "codename": "add_module",
      "name": "Can add \u041c\u043e\u0434\u0443\u043b\u044c"
    },
    {
      "id": 10,
      "content_type_id": 3,
      "codename": "change_module",
      "name": "Can change \u041c\u043e\u0434\u0443\u043b\u044c"
    },
    {
      "id": 11,
      "content_type_id": 3,
      "codename": "delete_module",
      "name": "Can delete \u041c\u043e\u0434\u0443\u043b\u044c"
    },
    {
      "id": 12,
      "content_type_id": 3,
      "codename": "view_module",
      "name": "Can view \u041c\u043e\u0434\u0443\u043b\u044c"
    },
    {
      "id": 13,
      "content_type_id": 4,
      "codename": "add_logentry",
      "name": "Can add log entry"
    },
    {
      "id": 14,
      "content_type_id": 4,
      "codename": "change_logentry",
      "name": "Can change log entry"
    },
    {
      "id": 15,
      "content_type_id": 4,
      "codename": "delete_logentry",
      "name": "Can delete log entry"
    },
    {
      "id": 16,
      "content_type_id": 4,
      "codename": "view_logentry",
      "name": "Can view log entry"
    },
    {
      "id": 17,
      "content_type_id": 5,
      "codename": "add_permission",
      "name": "Can add permission"
    },
    {
      "id": 18,
      "content_type_id": 5,
      "codename": "change_permission",
      "name": "Can change permission"
    },
    {
      "id": 19,
      "content_type_id": 5,
      "codename": "delete_permission",
      "name": "Can delete permission"
    },
    {
      "id": 20,
      "content_type_id": 5,
      "codename": "view_permission",
      "name": "Can view permission"
    },
    {
      "id": 21,
      "content_type_id": 6,
      "codename": "add_group",
      "name": "Can add group"
    },
    {
      "id": 22,
      "content_type_id": 6,
      "codename": "change_group",
      "name": "Can change group"
    },
    {
      "id": 23,
      "content_type_id": 6,
      "codename": "delete_group",
      "name": "Can delete group"
    },
    {
      "id": 24,
      "content_type_id": 6,
      "codename": "view_group",
      "name": "Can view group"
    },
    {
      "id": 25,
      "content_type_id": 7,
      "codename": "add_user",
      "name": "Can add user"
    },
    {
      "id": 26,
      "content_type_id": 7,
      "codename": "change_user",
      "name": "Can change user"
    },
    {
      "id": 27,
      "content_type_id": 7,
      "codename": "delete_user",
      "name": "Can delete user"
    },
    {
      "id": 28,
      "content_type_id": 7,
      "codename": "view_user",
      "name": "Can view user"
    },
    {
      "id": 29,
      "content_type_id": 8,
      "codename": "add_contenttype",
      "name": "Can add content type"
    },
    {
      "id": 30,
      "content_type_id": 8,
      "codename": "change_contenttype",
      "name": "Can change content type"
    },
    {
      "id": 31,
      "content_type_id": 8,
      "codename": "delete_contenttype",
      "name": "Can delete content type"
    },
    {
      "id": 32,
      "content_type_id": 8,
      "codename": "view_contenttype",
      "name": "Can view content type"
    },
    {
      "id": 33,
      "content_type_id": 9,
      "codename": "add_session",
      "name": "Can add session"
    },
    {
      "id": 34,
      "content_type_id": 9,
      "codename": "change_session",
      "name": "Can change session"
    },
    {
      "id": 35,
      "content_type_id": 9,
      "codename": "delete_session",
      "name": "Can delete session"
    },
    {
      "id": 36,
      "content_type_id": 9,
      "codename": "view_session",
      "name": "Can view session"
    },
    {
      "id": 37,
      "content_type_id": 10,
      "codename": "add_image",
      "name": "Can add \u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430"
    },
    {
      "id": 38,
      "content_type_id": 10,
      "codename": "change_image",
      "name": "Can change \u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430"
    },
    {
      "id": 39,
      "content_type_id": 10,
      "codename": "delete_image",
      "name": "Can delete \u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430"
    },
    {
      "id": 40,
      "content_type_id": 10,
      "codename": "view_image",
      "name": "Can view \u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430"
    },
    {
      "id": 41,
      "content_type_id": 11,
      "codename": "add_content",
      "name": "Can add \u041a\u043e\u043d\u0442\u0435\u043d\u0442"
    },
    {
      "id": 42,
      "content_type_id": 11,
      "codename": "change_content",
      "name": "Can change \u041a\u043e\u043d\u0442\u0435\u043d\u0442"
    },
    {
      "id": 43,
      "content_type_id": 11,
      "codename": "delete_content",
      "name": "Can delete \u041a\u043e\u043d\u0442\u0435\u043d\u0442"
    },
    {
      "id": 44,
      "content_type_id": 11,
      "codename": "view_content",
      "name": "Can view \u041a\u043e\u043d\u0442\u0435\u043d\u0442"
    },
    {
      "id": 45,
      "content_type_id": 12,
      "codename": "add_video",
      "name": "Can add \u0412\u0438\u0434\u0435\u043e"
    },
    {
      "id": 46,
      "content_type_id": 12,
      "codename": "change_video",
      "name": "Can change \u0412\u0438\u0434\u0435\u043e"
    },
    {
      "id": 47,
      "content_type_id": 12,
      "codename": "delete_video",
      "name": "Can delete \u0412\u0438\u0434\u0435\u043e"
    },
    {
      "id": 48,
      "content_type_id": 12,
      "codename": "view_video",
      "name": "Can view \u0412\u0438\u0434\u0435\u043e"
    },
    {
      "id": 49,
      "content_type_id": 13,
      "codename": "add_file",
      "name": "Can add \u0424\u0430\u0439\u043b"
    },
    {
      "id": 50,
      "content_type_id": 13,
      "codename": "change_file",
      "name": "Can change \u0424\u0430\u0439\u043b"
    },
    {
      "id": 51,
      "content_type_id": 13,
      "codename": "delete_file",
      "name": "Can delete \u0424\u0430\u0439\u043b"
    },
    {
      "id": 52,
      "content_type_id": 13,
      "codename": "view_file",
      "name": "Can view \u0424\u0430\u0439\u043b"
    },
    {
      "id": 53,
      "content_type_id": 14,
      "codename": "add_text",
      "name": "Can add \u0422\u0435\u043a\u0441\u0442"
    },
    {
      "id": 54,
      "content_type_id": 14,
      "codename": "change_text",
      "name": "Can change \u0422\u0435\u043a\u0441\u0442"
    },
    {
      "id": 55,
      "content_type_id": 14,
      "codename": "delete_text",
      "name": "Can delete \u0422\u0435\u043a\u0441\u0442"
    },
    {
      "id": 56,
      "content_type_id": 14,
      "codename": "view_text",
      "name": "Can view \u0422\u0435\u043a\u0441\u0442"
    }
  ],
  "auth_group": [
    {
      "id": 1,
      "name": "Teachers"
    }
  ],
  "auth_user": [
    {
      "id": 1,
      "password": "pbkdf2_sha256$1000000$9op1dsdJF0tYFUSphrTt7v$+BZ7kgqWkwCVnvs7SC+SLthIb1I+wvOmhvejFaUO6U8=",
      "last_login": "2025-12-23 16:00:45.808938",
      "is_superuser": 1,
      "username": "baranov",
      "last_name": "",
      "email": "",
      "is_staff": 1,
      "is_active": 1,
      "date_joined": "2025-09-26 14:17:00.892783",
      "first_name": ""
    },
    {
      "id": 5,
      "password": "pbkdf2_sha256$1000000$DJEUnwuLOwYagEBAEOVAHX$8Siqn4NeGR3oWt/HALOSk34+GZs24M/pfuBDwCByAis=",
      "last_login": "2026-01-09 11:59:21.383562",
      "is_superuser": 0,
      "username": "epstein",
      "last_name": "",
      "email": "",
      "is_staff": 0,
      "is_active": 1,
      "date_joined": "2025-12-23 09:07:28",
      "first_name": ""
    }
  ],
  "courses_subject": [
    {
      "id": 3,
      "title": "\u0412\u0435\u0440\u0441\u0442\u043a\u0430",
      "slug": "verstka"
    }
  ],
  "courses_course": [
    {
      "id": 10,
      "title": "HTML",
      "slug": "html",
      "overview": "\u041a\u0443\u0440\u0441 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f \u0432\u0435\u0440\u0441\u0442\u043a\u0438 \u043d\u0430 HTML",
      "created": "2025-12-23 09:09:38.672911",
      "owner_id": 5,
      "subject_id": 3
    },
    {
      "id": 11,
      "title": "CSS",
      "slug": "css",
      "overview": "\u041a\u0443\u0440\u0441 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f \u0441\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u0432\u0435\u0440\u0441\u0442\u043a\u0438 \u043d\u0430 CSS",
      "created": "2025-12-23 09:15:47.446481",
      "owner_id": 5,
      "subject_id": 3
    }
  ],
  "django_session": [
    {
      "session_key": "6s5wxrjs9w5tpfdkzjftdk9c5qr683m8",
      "session_data": ".eJxVjDsOwjAQRO_iGlmOiX-U9JzB2vWucQA5UpxUiLvjSCmgG817M28RYVtL3BovcSJxEVqcfjuE9OS6A3pAvc8yzXVdJpS7Ig_a5G0mfl0P9--gQCt9jYkJSTF67y1AsEabpM_gc06DygAWR91TYLRmIHTBUVA6u2BH24n4fAETMzhm:1vA7NB:JmazWzqFI0BYRVTZYAMsgnIqVpZlyQHHEP7jcZYHEQ4",
      "expire_date": "2025-11-01 13:53:29.531594"
    },
    {
      "session_key": "idf0o4oy2iyzfaesuktngeoo5s7x1mzv",
      "session_data": ".eJxVjDsOwjAQRO_iGlmOiX-U9JzB2vWucQA5UpxUiLvjSCmgG817M28RYVtL3BovcSJxEVqcfjuE9OS6A3pAvc8yzXVdJpS7Ig_a5G0mfl0P9--gQCt9jYkJSTF67y1AsEabpM_gc06DygAWR91TYLRmIHTBUVA6u2BH24n4fAETMzhm:1vBTjI:aW5bfAYY2yRINjvCiK2li0CnCypmOfOeWPlEju1jAaI",
      "expire_date": "2025-11-05 07:57:56.918010"
    },
    {
      "session_key": "3q0b1kl82czoe4fyigx6d840wo6bfe40",
      "session_data": ".eJxVjDsOwjAQRO_iGlmOiX-U9JzB2vWucQA5UpxUiLvjSCmgG817M28RYVtL3BovcSJxEVqcfjuE9OS6A3pAvc8yzXVdJpS7Ig_a5G0mfl0P9--gQCt9jYkJSTF67y1AsEabpM_gc06DygAWR91TYLRmIHTBUVA6u2BH24n4fAETMzhm:1vS9DM:opSLpyFN8zh8J209oAbIsFxgho7NIcYUDPsaOQnl3wc",
      "expire_date": "2025-12-21 07:29:52.841736"
    },
    {
      "session_key": "4grolwul9x0xubrmljqhf5p076qfdswk",
      "session_data": ".eJxVjEEOwiAQRe_C2hBAKNSl-56BDDODVA0kpV0Z765NutDtf-_9l4iwrSVunZc4k7gIJ06_WwJ8cN0B3aHemsRW12VOclfkQbucGvHzerh_BwV6-dYB6AxEicZxYAqkXHBKe6MZswaEYBn0oLJVGm22KWSlkrds2BrvAMX7AweXOII:1vXyO6:sW__qa9ACnL_qcaaeWpulDdX4k84xSzzGBEBj-mviAg",
      "expire_date": "2026-01-06 09:09:02.831592"
    },
    {
      "session_key": "kmwqi2z7ovzr6tp5jb7wsw71jxjaeub8",
      "session_data": ".eJxVjEEOwiAQRe_C2hBAKNSl-56BDDODVA0kpV0Z765NutDtf-_9l4iwrSVunZc4k7gIJ06_WwJ8cN0B3aHemsRW12VOclfkQbucGvHzerh_BwV6-dYB6AxEicZxYAqkXHBKe6MZswaEYBn0oLJVGm22KWSlkrds2BrvAMX7AweXOII:1vY4ov:z7TbZvRcYJV6rYADMKhTyTSGJ6Q8i8-6XEf4QRJcZ9I",
      "expire_date": "2026-01-06 16:01:09.539437"
    },
    {
      "session_key": "kzu5ja9l74nt1ycdonv1eysxk3fgi0zq",
      "session_data": ".eJxVjEEOwiAQRe_C2hBAKNSl-56BDDODVA0kpV0Z765NutDtf-_9l4iwrSVunZc4k7gIJ06_WwJ8cN0B3aHemsRW12VOclfkQbucGvHzerh_BwV6-dYB6AxEicZxYAqkXHBKe6MZswaEYBn0oLJVGm22KWSlkrds2BrvAMX7AweXOII:1veB9F:t7BCLosc_GNAF8OkRVkH1REnH2piR1Yjhzg9AetLwvg",
      "expire_date": "2026-01-23 11:59:21.388555"
    }
  ],
  "courses_file": [],
  "courses_image": [
    {
      "id": 5,
      "title": "",
      "created": "2025-12-23 10:06:48.050417",
      "updated": "2025-12-23 10:06:48.050417",
      "file": "images/capture_20251223170505147.bmp",
      "owner_id": 5
    },
    {
      "id": 6,
      "title": "",
      "created": "2025-12-23 10:06:53.682790",
      "updated": "2025-12-23 10:06:53.682790",
      "file": "images/capture_20251223170526900.bmp",
      "owner_id": 5
    },
    {
      "id": 7,
      "title": "",
      "created": "2025-12-23 10:07:00.979891",
      "updated": "2025-12-23 10:07:00.979891",
      "file": "images/capture_20251223170618084.bmp",
      "owner_id": 5
    },
    {
      "id": 8,
      "title": "",
      "created": "2025-12-23 10:13:31.032499",
      "updated": "2025-12-23 10:13:31.032499",
      "file": "images/capture_20251223171307581.bmp",
      "owner_id": 5
    },
    {
      "id": 9,
      "title": "",
      "created": "2025-12-23 10:16:39.401151",
      "updated": "2025-12-23 10:16:39.401151",
      "file": "images/capture_20251223171615866.bmp",
      "owner_id": 5
    }
  ],
  "courses_text": [
    {
      "id": 19,
      "title": "",
      "created": "2025-12-23 09:34:00.408261",
      "updated": "2025-12-23 10:02:24.895856",
      "content": "\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430. \u0422\u0435\u0433\u0438 \u0438 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u044b\r\nHyperText Markup Language - \u044f\u0437\u044b\u043a \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0438 \u0433\u0438\u043f\u0435\u0440\u0442\u0435\u043a\u0441\u0442\u0430. \u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430 HTML \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430 - \u0441\u043a\u0435\u043b\u0435\u0442, \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0441\u0442\u0440\u043e\u0438\u0442\u0441\u044f \u0432\u0441\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430:\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <head>\r\n    <meta charset=\"utf-8\">\r\n    <title>\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430</title>\r\n  </head>\r\n  <body>\r\n    <h1>...</h1>\r\n    <p>...</p>\r\n  </body>\r\n</html>\r\n\r\n!DOCTYPE\r\n\u041f\u0435\u0440\u0432\u044b\u043c \u0442\u0435\u0433\u043e\u043c \u0432 \u043b\u044e\u0431\u043e\u043c HTML \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0435 \u0434\u043e\u043b\u0436\u0435\u043d \u0438\u0434\u0442\u0438 \u0442\u0435\u0433 !DOCTYPE. \u041e\u043d \u0433\u043e\u0432\u043e\u0440\u0438\u0442 \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0443, \u043f\u043e \u043a\u0430\u043a\u043e\u043c\u0443 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u0443 \u043d\u0430\u043f\u0438\u0441\u0430\u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430.\r\n\r\n\r\nhtml\r\n\u0412\u0442\u043e\u0440\u044b\u043c \u0442\u0435\u0433\u043e\u043c \u0438\u0434\u0435\u0442 html - \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u0434\u0432\u0430 \u0442\u0435\u0433\u0430 - head \u0438 body. HTML-\u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0434\u043e\u043b\u0436\u043d\u0430 \u0437\u0430\u043a\u0430\u043d\u0447\u0438\u0432\u0430\u0442\u044c\u0441\u044f \u0437\u0430\u043a\u0440\u044b\u0442\u044b\u043c \u0442\u0435\u0433\u043e\u043c /html.\r\n\r\nhead\r\n\u0412 \u0442\u0435\u0433\u0435 head \u0445\u0440\u0430\u043d\u0438\u0442\u0441\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435. \u0417\u0434\u0435\u0441\u044c \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0442 \u043a\u043e\u0434\u0438\u0440\u043e\u0432\u043a\u0443 meta charset=\"...\", \u0438\u043c\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b title.../title, \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u0443\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u043e\u0432\u0438\u043a\u043e\u0432, \u0430 \u0435\u0449\u0451 \u0442\u0443\u0442 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0430\u044e\u0442\u0441\u044f \u0441\u0442\u0438\u043b\u0435\u0432\u044b\u0435 \u0444\u0430\u0439\u043b\u044b \u0438 \u0441\u043a\u0440\u0438\u043f\u0442\u044b.\u0422\u0435\u0433 \u043d\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f. \u0415\u0433\u043e \u0446\u0435\u043b\u044c \u2014 \u0441\u043a\u0430\u0437\u0430\u0442\u044c \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0443 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435.\r\n\r\n\r\nbody\r\n\u0412 \u0442\u0435\u0433\u0435 \u0440\u0430\u0437\u043c\u0435\u0449\u0430\u0435\u0442\u0441\u044f \u0432\u0435\u0441\u044c \u043a\u043e\u043d\u0442\u0435\u043d\u0442 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0443\u0432\u0438\u0434\u0438\u0442 \u0432 \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0435.\r\n\r\n\r\n\u0422\u0435\u0433\u0438\r\n\u0422\u0435\u0433 \u2014 \u044d\u0442\u043e \u0441\u0438\u043d\u0442\u0430\u043a\u0441\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0435\u0434\u0438\u043d\u0438\u0446\u0430 \u044f\u0437\u044b\u043a\u0430 HTML, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0432\u044b\u0434\u0435\u043b\u044f\u0435\u0442 \u0438\u043b\u0438 \u0441\u043e\u0437\u0434\u0430\u0451\u0442 \u044d\u043b\u0435\u043c\u0435\u043d\u0442. \u0415\u0441\u0442\u044c 2 \u0432\u0438\u0434\u0430 \u0442\u0435\u0433\u043e\u0432: \u0434\u0432\u043e\u0439\u043d\u044b\u0435 \u0438 \u043e\u0434\u0438\u043d\u0430\u0440\u043d\u044b\u0435\r\n\r\n\r\n\u0414\u0432\u043e\u0439\u043d\u044b\u0435 \u0442\u0435\u0433\u0438\r\n\u0414\u0432\u043e\u0439\u043d\u044b\u0435 \u0442\u0435\u0433\u0438 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u043d\u0430\u0447\u0430\u043b\u043e \u0438 \u043a\u043e\u043d\u0435\u0446 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430. \u041d\u0430\u0447\u0430\u043b\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0430\u0435\u0442\u0441\u044f \u043e\u0442\u043a\u0440\u044b\u0432\u0430\u044e\u0449\u0438\u043c \u0442\u0435\u0433\u043e\u043c <\u2026> , \u0430 \u043a\u043e\u043d\u0435\u0446 - \u0437\u0430\u043a\u0440\u044b\u0432\u0430\u044e\u0449\u0438\u043c .\r\n\r\n\r\n\u041e\u0434\u0438\u043d\u0430\u0440\u043d\u044b\u0435 \u0442\u0435\u0433\u0438\r\n\u041e\u0434\u0438\u043d\u0430\u0440\u043d\u044b\u0435 \u0442\u0435\u0433\u0438 \u043f\u0440\u043e\u0441\u0442\u043e \u043d\u0435 \u0438\u043c\u0435\u044e\u0442 \u043f\u0430\u0440\u044b. \u041f\u0440\u0438\u043c\u0435\u0440\u044b: \u0442\u0435\u0433 \u043f\u0435\u0440\u0435\u043d\u043e\u0441\u0430 \u0441\u0442\u0440\u043e\u043a\u0438 br \u0438\u043b\u0438 \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u043b\u0438\u043d\u0438\u0438 hr.\r\n\r\n\r\n\u0410\u0442\u0440\u0438\u0431\u0443\u0442\u044b\r\n\u0410\u0442\u0440\u0438\u0431\u0443\u0442\u044b \u2014 \u044d\u0442\u043e \u0441\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u0442\u0435\u0433\u0430. \u0421 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043d\u0438\u0445 \u043c\u044b \u0437\u0430\u0434\u0430\u0451\u043c \u0435\u0433\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b.\r\n\r\n\r\n\u0412\u043e\u0437\u044c\u043c\u0451\u043c \u043f\u0440\u0438\u043c\u0435\u0440: \u0442\u0435\u0433 a \u2014 \u0441\u0441\u044b\u043b\u043a\u0430. \u0414\u043b\u044f \u0437\u0430\u0434\u0430\u043d\u0438\u044f \u0430\u0434\u0440\u0435\u0441\u0430, \u043a\u0443\u0434\u0430 \u0431\u0443\u0434\u0435\u0442 \u0432\u0435\u0441\u0442\u0438 \u044d\u0442\u0430 \u0441\u0441\u044b\u043b\u043a\u0430, \u043d\u0430\u043c \u043f\u043e\u043d\u0430\u0434\u043e\u0431\u0438\u0442\u0441\u044f \u0430\u0442\u0440\u0438\u0431\u0443\u0442 href. \u0412\u043e\u0442 \u0442\u0430\u043a \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u0433\u043b\u044f\u0434\u0435\u0442\u044c \u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443 Google:\r\n\r\n\r\n<a href=\"http://google.com\">\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0433\u0443\u0433\u043b</a>\r\n\r\n\r\n\u0412 \u0442\u0435\u0433\u0435 \u0442\u0430\u043a\u0436\u0435 \u043c\u043e\u0436\u0435\u0442 \u0438 \u043d\u0435 \u0431\u044b\u0442\u044c \u043d\u0438 \u043a\u0430\u043a\u0438\u0445 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u043e\u0432.",
      "owner_id": 5
    },
    {
      "id": 20,
      "title": "",
      "created": "2025-12-23 09:45:27.666673",
      "updated": "2025-12-23 09:49:10.299878",
      "content": "\u0411\u043b\u043e\u0447\u043d\u044b\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b\r\n\u0421\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u044e\u0442 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0443 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b.\r\n\r\n\u041e\u0441\u043e\u0431\u0435\u043d\u043d\u043e\u0441\u0442\u0438:\r\n-\u0431\u043b\u043e\u043a\u0438 \u0440\u0430\u0441\u043f\u043e\u043b\u0430\u0433\u0430\u044e\u0442\u0441\u044f \u0434\u0440\u0443\u0433 \u043f\u043e\u0434 \u0434\u0440\u0443\u0433\u043e\u043c \u043f\u043e \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u0438\r\n-\u0437\u0430\u043f\u0440\u0435\u0449\u0435\u043d\u043e \u0432\u0441\u0442\u0430\u0432\u043b\u044f\u0442\u044c \u0431\u043b\u043e\u0447\u043d\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442 \u0432\u043d\u0443\u0442\u0440\u044c \u0441\u0442\u0440\u043e\u0447\u043d\u043e\u0433\u043e\r\n-\u0437\u0430\u043d\u0438\u043c\u0430\u044e\u0442 \u0432\u0441\u0451 \u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u043e\u0435 \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u043e \u043f\u043e \u0448\u0438\u0440\u0438\u043d\u0435\r\n-\u0432\u044b\u0441\u043e\u0442\u0430 \u0432\u044b\u0447\u0438\u0441\u043b\u044f\u0435\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438, \u0438\u0441\u0445\u043e\u0434\u044f \u0438\u0437 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0433\u043e\r\n\r\n\u041f\u0440\u0438\u043c\u0435\u0440\u044b:\r\n-\u0430\u0431\u0437\u0430\u0446\u044b <\u0440>\r\n-\u0441\u043f\u0438\u0441\u043a\u0438: \u043c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 <ul> \u0438 \u043d\u0443\u043c\u0435\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 <ol>\r\n-\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438: \u043e\u0442 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f <h1> \u0434\u043e \u0448\u0435\u0441\u0442\u043e\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f <h6>\r\n-\u0441\u0442\u0430\u0442\u044c\u0438 <article>\r\n-\u0440\u0430\u0437\u0434\u0435\u043b\u044b <section>\r\n-\u0434\u043b\u0438\u043d\u043d\u044b\u0435 \u0446\u0438\u0442\u0430\u0442\u044b <blockquote>\r\n-\u0431\u043b\u043e\u043a\u0438 \u043e\u0431\u0449\u0435\u0433\u043e \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f  <div>\r\n\r\n\u0421\u0442\u0440\u043e\u0447\u043d\u044b\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b:\r\n\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442\u0441\u044f \u0434\u043b\u044f \u0444\u043e\u0440\u043c\u0430\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0445 \u0444\u0440\u0430\u0433\u043c\u0435\u043d\u0442\u043e\u0432. \u041e\u0431\u044b\u0447\u043d\u043e \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0442 \u043e\u0434\u043d\u043e \u0438\u043b\u0438 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0441\u043b\u043e\u0432.\r\n\r\n\u041e\u0441\u043e\u0431\u0435\u043d\u043d\u043e\u0441\u0442\u0438:\r\n-\u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b, \u0438\u0434\u0443\u0449\u0438\u0435 \u043f\u043e\u0434\u0440\u044f\u0434, \u0440\u0430\u0441\u043f\u043e\u043b\u0430\u0433\u0430\u044e\u0442\u0441\u044f \u043d\u0430 \u043e\u0434\u043d\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0435 \u0438 \u043f\u0435\u0440\u0435\u043d\u043e\u0441\u044f\u0442\u0441\u044f \u043d\u0430 \u0434\u0440\u0443\u0433\u0443\u044e \u043f\u0440\u0438 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u0438\r\n-\u0432\u043d\u0443\u0442\u0440\u044c \u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u043e \u0432\u0441\u0442\u0430\u0432\u043b\u044f\u0442\u044c \u0442\u0435\u043a\u0441\u0442 \u0438\u043b\u0438 \u0434\u0440\u0443\u0433\u0438\u0435 \u0441\u0442\u0440\u043e\u0447\u043d\u044b\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b, \u043f\u043e\u043c\u0435\u0449\u0430\u0442\u044c \u0431\u043b\u043e\u0447\u043d\u044b\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b - \u0437\u0430\u043f\u0440\u0435\u0449\u0435\u043d\u043e\r\n\r\n\u041f\u0440\u0438\u043c\u0435\u0440\u044b:\r\n-\u0441\u0441\u044b\u043b\u043a\u0438 <a>\r\n-\u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0435 \u0441\u043b\u043e\u0432\u0430 <em>\r\n-\u0432\u0430\u0436\u043d\u044b\u0435 \u0441\u043b\u043e\u0432\u0430 <strong>\r\n-\u043a\u043e\u0440\u043e\u0442\u043a\u0438\u0435 \u0446\u0438\u0442\u0430\u0442\u044b <q>\r\n-\u0430\u0431\u0431\u0440\u0435\u0432\u0438\u0430\u0442\u0443\u0440\u044b <abbr>",
      "owner_id": 5
    },
    {
      "id": 21,
      "title": "",
      "created": "2025-12-23 09:53:53.563542",
      "updated": "2025-12-23 10:02:55.797150",
      "content": "\u0412 HTML \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442 \u0442\u0440\u0438 \u0432\u0438\u0434\u0430 \u0441\u043f\u0438\u0441\u043a\u043e\u0432:\r\n-\u041c\u0430\u0440\u043a\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439\r\n-\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u0437 \u043d\u0435\u0443\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0435\u043d\u043d\u044b\u0445 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432.\r\n\r\n\u0421\u043e\u0441\u0442\u043e\u0438\u0442 \u0438\u0437 \u0434\u0432\u0443\u0445 \u0442\u0435\u0433\u043e\u0432:\r\n<ul> (unordered list) - \u0442\u0435\u0433 \u043d\u0430\u0447\u0430\u043b\u0430 \u0438 \u043a\u043e\u043d\u0446\u0430 \u0441\u043f\u0438\u0441\u043a\u0430\r\n<li> (list item) - \u043f\u0443\u043d\u043a\u0442 \u0441\u043f\u0438\u0441\u043a\u0430\r\n\u041f\u0440\u0438\u043c\u0435\u0440:\r\n\r\n\t<ul>\r\n\t\t<li>\u041a\u0430\u0440\u0442\u043e\u0448\u043a\u0430</li>\r\n\t\t<li>\u041c\u043e\u0440\u043a\u043e\u0432\u043a\u0430</li>\r\n\t\t<li>\u0421\u0432\u0435\u043a\u043b\u0430</li>\r\n\t</ul>",
      "owner_id": 5
    },
    {
      "id": 22,
      "title": "",
      "created": "2025-12-23 09:55:51.430073",
      "updated": "2025-12-23 10:03:13.982485",
      "content": "\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0439\r\n\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442\u0441\u044f \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0441\u043f\u0438\u0441\u043a\u0430 \u0442\u0435\u0440\u043c\u0438\u043d\u043e\u0432 \u0438 \u0438\u0445 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0439. \u0412 \u043e\u0431\u0449\u0435\u043c \u0441\u043b\u0443\u0447\u0430\u0435, \u043a\u0430\u0436\u0434\u044b\u0439 \u043f\u0443\u043d\u043a\u0442 \u2014 \u044d\u0442\u043e \u043f\u0430\u0440\u0430 \"\u0438\u043c\u044f/\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435\".\r\n\r\n\u0421\u043e\u0441\u0442\u043e\u0438\u0442 \u0438\u0437 \u0442\u0440\u0451\u0445 \u0442\u0435\u0433\u043e\u0432:\r\n<dl> (description list) - \u0442\u0435\u0433 \u043d\u0430\u0447\u0430\u043b\u0430 \u0438 \u043a\u043e\u043d\u0446\u0430 \u0441\u043f\u0438\u0441\u043a\u0430\r\n<dt> (term) - \u0442\u0435\u0440\u043c\u0438\u043d\r\n<dd> (description) - \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435\r\n\u041f\u0440\u0438\u043c\u0435\u0440:\r\n\r\n<dl>\r\n\t\t<dt>\u0413\u0430\u0441\u043f\u0430\u0447\u043e</dt>\r\n\t\t\t<dd>\u043b\u0451\u0433\u043a\u0438\u0439 \u0445\u043e\u043b\u043e\u0434\u043d\u044b\u0439 \u0441\u0443\u043f \u0438\u0437 \u043f\u0435\u0440\u0435\u0442\u0451\u0440\u0442\u044b\u0445 \u0432 \u043f\u044e\u0440\u0435 \u0441\u0432\u0435\u0436\u0438\u0445 \u043e\u0432\u043e\u0449\u0435\u0439</dd>\r\n\t\t<dt>\u0422\u043e\u043c-\u044f\u043c</dt>\r\n\t\t\t<dd>\u043a\u0438\u0441\u043b\u043e-\u043e\u0441\u0442\u0440\u044b\u0439 \u0441\u0443\u043f \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u043a\u0443\u0440\u0438\u043d\u043e\u0433\u043e \u0431\u0443\u043b\u044c\u043e\u043d\u0430 \u0441 \u043a\u0440\u0435\u0432\u0435\u0442\u043a\u0430\u043c\u0438, \u043a\u0443\u0440\u0438\u0446\u0435\u0439, \u0440\u044b\u0431\u043e\u0439 \u0438\u043b\u0438 \u0434\u0440\u0443\u0433\u0438\u043c\u0438 \u043c\u043e\u0440\u0435\u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430\u043c\u0438</dd>\r\n\t\t<dt>\u0411\u043e\u0440\u0449</dt>\r\n\t\t\t<dd>\u0440\u0430\u0437\u043d\u043e\u0432\u0438\u0434\u043d\u043e\u0441\u0442\u044c \u0441\u0443\u043f\u0430 \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u0441\u0432\u0451\u043a\u043b\u044b, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u043f\u0440\u0438\u0434\u0430\u0451\u0442 \u0431\u043e\u0440\u0449\u0443 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u043d\u044b\u0439 \u043a\u0440\u0430\u0441\u043d\u044b\u0439 \u0446\u0432\u0435\u0442</dd>\r\n\t</dl>",
      "owner_id": 5
    },
    {
      "id": 23,
      "title": "",
      "created": "2025-12-23 10:04:01.777981",
      "updated": "2025-12-23 10:04:49.196399",
      "content": "\u041d\u0443\u043c\u0435\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439\r\n\u0423\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0435\u043d\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a, \u043a\u0430\u0436\u0434\u044b\u0439 \u043f\u0443\u043d\u043a\u0442 \u0438\u043c\u0435\u0435\u0442 \u0441\u0432\u043e\u0439 \u043d\u043e\u043c\u0435\u0440.\r\n\r\n\u0421\u043e\u0441\u0442\u043e\u0438\u0442 \u0438\u0437 \u0434\u0432\u0443\u0445 \u0442\u0435\u0433\u043e\u0432:\r\n<ol> (ordered list) - \u0442\u0435\u0433 \u043d\u0430\u0447\u0430\u043b\u0430 \u0438 \u043a\u043e\u043d\u0446\u0430 \u0441\u043f\u0438\u0441\u043a\u0430\r\n<li> (list item) - \u043f\u0443\u043d\u043a\u0442 \u0441\u043f\u0438\u0441\u043a\u0430\r\n\r\n\u041f\u0440\u0438\u043c\u0435\u0440:\r\n\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u043f\u043e \u043f\u0440\u0438\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d\u0438\u044e:\r\n\r\n<ol>\r\n <li>\u0414\u043e\u0432\u0435\u0441\u0442\u0438 \u0432\u043e\u0434\u0443 \u0434\u043e \u043a\u0438\u043f\u0435\u043d\u0438\u044f</li>\r\n <li>\u0417\u0430\u0441\u044b\u043f\u0430\u0442\u044c \u0438\u043d\u0433\u0440\u0435\u0434\u0438\u0435\u043d\u0442\u044b</li>\r\n <li>\u0412\u0430\u0440\u0438\u0442\u044c 10 \u043c\u0438\u043d\u0443\u0442</li>\r\n</ol>\r\n\r\n\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b:",
      "owner_id": 5
    },
    {
      "id": 24,
      "title": "",
      "created": "2025-12-23 10:10:08.876281",
      "updated": "2025-12-23 10:13:25.025103",
      "content": "\u0414\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0442\u0435\u0433 <img>. \u042d\u0442\u043e \u043e\u0434\u0438\u043d\u0430\u0440\u043d\u044b\u0439 \u0442\u0435\u0433. \u0412\u043e\u0442 \u0435\u0433\u043e \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u044b:\r\n\r\nsrc - \u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443\ufeff\r\nalt - \u0442\u0435\u043a\u0441\u0442, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u0432\u043c\u0435\u0441\u0442\u043e \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438, \u0435\u0441\u043b\u0438 \u043e\u043d\u0430 \u043d\u0435 \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u043b\u0430\u0441\u044c\r\ntitle - \u0442\u0435\u043a\u0441\u0442, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043c\u044b\u0448\u0438 \u043d\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443\r\nwidth - \u0448\u0438\u0440\u0438\u043d\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0432 \u043f\u0438\u043a\u0441\u0435\u043b\u044f\u0445\r\nheight - \u0432\u044b\u0441\u043e\u0442\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0432 \u043f\u0438\u043a\u0441\u0435\u043b\u044f\u0445\r\n\u041f\u0440\u0438\u043c\u0435\u0440:\r\n\r\n<img\r\n src=\"http://example.com/cat.jpg\"\r\n title=\"\u041c\u0443\u0440\u043a\u0430\"\r\n alt=\"\u0420\u044b\u0436\u0430\u044f \u043a\u043e\u0448\u043a\u0430 \u0432\u0430\u043b\u044f\u0435\u0442\u0441\u044f \u0432 \u0441\u043d\u0435\u0433\u0443\"\r\n width=\"640\"\r\n height=\"480\"\r\n>\r\n \r\n-\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0441 \u043f\u043e\u0434\u043f\u0438\u0441\u044c\u044e \u0432 HTML 5\r\n\u0412 HTML 5 \u043f\u043e\u044f\u0432\u0438\u043b\u0438\u0441\u044c \u0442\u0435\u0433\u0438 \u0434\u043b\u044f \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u044f \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \ufeff\u0441 \u043f\u043e\u0434\u043f\u0438\u0441\u044f\u043c\u0438\ufeff - figure \u0438 figcaption. \u0415\u0441\u043b\u0438 \u0442\u0432\u043e\u0435\u0439 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0435 \u043d\u0443\u0436\u043d\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u044c - \u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0441\u044f \u0438\u043c\u0438. \u041f\u0440\u0438\u043c\u0435\u0440 \u043a\u043e\u0434\u0430:\r\n\r\n<figure>\r\n  <img src=\"(\u043f\u043e\u043b\u043d\u044b\u0439 \u043f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f)\">\r\n  <figcaption>\r\n    \u0424\u043e\u0442\u043a\u0430 \u0420\u043e\u043d\u0430\u043b\u044c\u0434\u043e\r\n  </figcaption>\r\n\ufeff</figure>\r\n\r\n\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:",
      "owner_id": 5
    },
    {
      "id": 25,
      "title": "",
      "created": "2025-12-23 10:15:25.885971",
      "updated": "2025-12-23 10:15:38.339521",
      "content": "\u0422\u0430\u0431\u043b\u0438\u0446\u044b \u0432 HTML \u0441\u043e\u0437\u0434\u0430\u044e\u0442\u0441\u044f \u043f\u0440\u0438 \u043f\u043e\u043c\u043e\u0449\u0438 \u0442\u0435\u0433\u0430 <table>.\r\n\u0412\u043d\u0443\u0442\u0440\u0438 \u043d\u0435\u0433\u043e \u0440\u0430\u0437\u043c\u0435\u0449\u0430\u044e\u0442 \u0441\u0442\u0440\u043e\u043a\u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u044b <tr> (table row)\r\n\u0412\u043d\u0443\u0442\u0440\u0438 \u0441\u0442\u0440\u043e\u043a \u043f\u043e\u043c\u0435\u0449\u0430\u044e\u0442 \u044f\u0447\u0435\u0439\u043a\u0438 \u0441\u0442\u0440\u043e\u043a\u0438 <td> (table data).\r\n\r\n\u0422\u0435\u0433\u043e\u043c <th> (table header) \u0440\u0430\u0437\u043c\u0435\u0447\u0430\u044e\u0442\u0441\u044f \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u0447\u043d\u044b\u0435 \u044f\u0447\u0435\u0439\u043a\u0438. \u041e\u043d \u043e\u0442\u043b\u0438\u0447\u0430\u0435\u0442\u0441\u044f \u043e\u0442 <td> \u0442\u0435\u043c, \u0447\u0442\u043e \u0435\u0433\u043e \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043e \u043f\u043e\u043b\u0443\u0436\u0438\u0440\u043d\u044b\u043c \u0438 \u0432\u044b\u0440\u043e\u0432\u043d\u0435\u043d\u043e \u043f\u043e \u0446\u0435\u043d\u0442\u0440\u0443.\r\n\r\n\u041f\u0440\u0438\u043c\u0435\u0440 \u0442\u0430\u0431\u043b\u0438\u0446\u044b:\r\n\r\n<table>\r\n  <tr>\r\n    <th>\u0418\u043c\u044f</th>\r\n    <th>\u0412\u043e\u0437\u0440\u0430\u0441\u0442</th> \r\n    <th>\u0421\u0443\u043f\u0435\u0440\u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u044c</th>\r\n  </tr>\r\n  <tr>\r\n    <td>\u041b\u043e\u0433\u0430\u043d</td>\r\n    <td>186</td> \r\n    <td>\u041f\u043e\u0432\u044b\u0448\u0435\u043d\u043d\u0430\u044f \u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u044c \u043a \u0440\u0435\u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u0438</td>\r\n  </tr>\r\n  <tr>\r\n    <td>\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u043e\u0440 \u0438\u043a\u0441</td>\r\n      <td>94</td>\r\n    <td>\u0427\u0442\u0435\u043d\u0438\u0435 \u043c\u044b\u0441\u043b\u0435\u0439, \u0432\u044b\u0437\u043e\u0432 \u0438\u043b\u043b\u044e\u0437\u0438\u0439, \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u043f\u0430\u0440\u0430\u043b\u0438\u0447\u0430, \u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u044c \u043e\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0442\u044c \u0432\u0440\u0435\u043c\u044f</td> \r\n  </tr>\r\n</table>\r\n\r\n\u0412\u0430\u0436\u043d\u043e!!!\r\n\u0410\u0442\u0440\u0438\u0431\u0443\u0442 border \u0443\u0441\u0442\u0430\u0440\u0435\u043b \u0438 \u0435\u0433\u043e \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0432 HTML5 \u043d\u0435 \u043f\u0440\u0438\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442\u0441\u044f. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0439 \u0430\u0442\u0440\u0438\u0431\u0443\u0442 \u0442\u043e\u043b\u044c\u043a\u043e \u043f\u043e\u043a\u0430 \u0437\u043d\u0430\u043a\u043e\u043c\u0438\u0442\u0435\u0441\u044c \u0441 \u0442\u0430\u0431\u043b\u0438\u0446\u0430\u043c\u0438. \u0414\u0430\u043d\u043d\u044b\u0439 \u0430\u0442\u0440\u0438\u0431\u0443\u0442 \u0437\u0430\u043c\u0435\u043d\u044f\u0435\u0442 \u0441\u0432\u043e\u0439\u0441\u0442\u0432\u043e border \u0432 CSS.\r\n\r\n\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:",
      "owner_id": 5
    },
    {
      "id": 26,
      "title": "",
      "created": "2025-12-23 10:27:41.256696",
      "updated": "2025-12-23 10:27:41.256696",
      "content": "\u0422\u044b \u0443\u0436\u0435 \u0437\u043d\u0430\u043a\u043e\u043c \u0441\u043e \u0441\u0441\u044b\u043b\u043a\u0430\u043c\u0438:\r\n\r\n<a href=\"https://google.com/\">Google</a>\r\n\r\n\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u043c: \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0441\u0441\u044b\u043b\u043a\u0438 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0442\u0435\u0433 <a>. \u0410\u0442\u0440\u0438\u0431\u0443\u0442 href \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u0430\u0434\u0440\u0435\u0441, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u0431\u0443\u0434\u0435\u0442 \u0441\u043e\u0432\u0435\u0440\u0448\u0451\u043d \u043f\u0435\u0440\u0435\u0445\u043e\u0434.\r\n\r\n\u0410\u0434\u0440\u0435\u0441\u0430 \u0431\u044b\u0432\u0430\u044e\u0442 \u0434\u0432\u0443\u0445 \u0432\u0438\u0434\u043e\u0432:\r\n-\u0410\u0431\u0441\u043e\u043b\u044e\u0442\u043d\u044b\u0435 \u0430\u0434\u0440\u0435\u0441\u0430\r\n\u0410\u0431\u0441\u043e\u043b\u044e\u0442\u043d\u044b\u0439 \u0430\u0434\u0440\u0435\u0441, \u0437\u0430\u043f\u0438\u0441\u0430\u043d\u043d\u044b\u0439 \u0432 \u043f\u043e\u043b\u043d\u043e\u0439 \u0444\u043e\u0440\u043c\u0435. \r\n\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440\r\n\r\nhttps://google.com/doodles\r\n\r\n\u0414\u0430\u0432\u0430\u0439 \u0440\u0430\u0437\u0431\u0435\u0440\u0451\u043c \u044d\u0442\u043e\u0442 \u0430\u0434\u0440\u0435\u0441:\r\nhttps - \u0442\u0430\u043a \u043d\u0430\u0437\u044b\u0432\u0430\u0435\u043c\u0430\u044f \u00ab\u0441\u0445\u0435\u043c\u0430\u00bb, \u043e\u0431\u044b\u0447\u043d\u043e \u044d\u0442\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0442\u043e\u043a\u043e\u043b\u0430. HTTPS - \u0437\u0430\u0449\u0438\u0449\u0451\u043d\u043d\u0430\u044f \u0432\u0435\u0440\u0441\u0438\u044f HTTP\r\ngoogle.com - \u0434\u043e\u043c\u0435\u043d\u043d\u043e\u0435 \u0438\u043c\u044f \u0441\u0430\u0439\u0442\u0430\r\n/doodles - \u043f\u0443\u0442\u044c (\u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044f) \u0432\u043d\u0443\u0442\u0440\u0438 \u0441\u0430\u0439\u0442\u0430\r\n\u0415\u0449\u0451 \u043f\u0440\u0438\u043c\u0435\u0440:\r\n\r\nfile:///C:/Users/admin/Desktop/\u041d\u043e\u0432\u0430\u044f%20\u043f\u0430\u043f\u043a\u0430/image.jpg\r\nfile - \u0441\u0445\u0435\u043c\u0430 URI, \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u0430\u044f \u0434\u043b\u044f \u0442\u043e\u0433\u043e, \u0447\u0442\u043e\u0431\u044b \u0430\u0434\u0440\u0435\u0441\u043e\u0432\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b \u043d\u0430 \u043b\u043e\u043a\u0430\u043b\u044c\u043d\u043e\u043c \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0435 \u0438\u043b\u0438 \u0432 \u043b\u043e\u043a\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0442\u0438 (\u043f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435 \u043d\u0430 \u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u0438)\r\n/C:/Users/admin/Desktop/\u041d\u043e\u0432\u0430\u044f%20\u043f\u0430\u043f\u043a\u0430/image.jpg - \u043f\u0443\u0442\u044c \u0434\u043e \u0444\u0430\u0439\u043b\u0430. %20 - \u043a\u043e\u0434 \u043f\u0440\u043e\u0431\u0435\u043b\u0430 \u0432 URI-\u043a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0438.\r\n\r\n-\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0430\u0434\u0440\u0435\u0441\u0430\r\n\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 - \u0441\u043e\u043a\u0440\u0430\u0449\u0451\u043d\u043d\u044b\u0439 \u0430\u0434\u0440\u0435\u0441. \u0412 \u0442\u0430\u043a\u043e\u043c \u0430\u0434\u0440\u0435\u0441\u0435 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u044c \u043e\u043f\u0443\u0449\u0435\u043d\u0430 \u0438 \u0431\u0440\u0430\u0443\u0437\u0435\u0440 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u0430\u0434\u0440\u0435\u0441 \u0434\u043b\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043f\u043e\u043b\u043d\u043e\u0433\u043e \u0430\u0434\u0440\u0435\u0441\u0430. \r\n\u041f\u0440\u0438\u043c\u0435\u0440\u044b:\r\n\r\n//google.com - \u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0434\u043e\u043c\u0435\u043d \u0432 \u0442\u0435\u043a\u0443\u0449\u0435\u043c \u043f\u0440\u043e\u0442\u043e\u043a\u043e\u043b\u0435: \u0435\u0441\u043b\u0438 \u043c\u044b \u043d\u0430\u0445\u043e\u0434\u0438\u043c\u0441\u044f \u043f\u043e \u0430\u0434\u0440\u0435\u0441\u0443, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442\u0441\u044f \u0441 http, \u0442\u043e \u0441\u0441\u044b\u043b\u043a\u0430 \u0431\u0443\u0434\u0435\u0442 \u0432\u0435\u0441\u0442\u0438 \u043d\u0430 http://google.com\r\n/sheets - \u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043f\u0443\u0442\u044c \u0432\u043d\u0443\u0442\u0440\u0438 \u0442\u0435\u043a\u0443\u0449\u0435\u0433\u043e \u0434\u043e\u043c\u0435\u043d\u0430: \u0435\u0441\u043b\u0438 \u043c\u044b \u043d\u0430\u0445\u043e\u0434\u0438\u043c\u0441\u044f \u043d\u0430 http://google.com, \u0442\u043e \u0441\u0441\u044b\u043b\u043a\u0430 \u0431\u0443\u0434\u0435\u0442 \u0432\u0435\u0441\u0442\u0438 \u043d\u0430 http://google.com/sheets, \u0430 \u0435\u0441\u043b\u0438 \u043d\u0430 http://facebook.com, \u0442\u043e \u043d\u0430 http://facebook.com/sheets.\r\npage2 - \u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043f\u0443\u0442\u044c \u0432\u043d\u0443\u0442\u0440\u0438 \u0442\u0435\u043a\u0443\u0449\u0435\u0439 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u0438: \u0435\u0441\u043b\u0438 \u043c\u044b \u043d\u0430\u0445\u043e\u0434\u0438\u043c\u0441\u044f \u043d\u0430 http://site.com/routes/page1, \u0442\u043e \u043f\u043e\u043f\u0430\u0434\u0451\u043c \u043d\u0430 http://site.com/routes/page2\r\n\r\n\u041f\u0440\u0438\u043c\u0435\u0440 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044f \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u0430\u0434\u0440\u0435\u0441\u0430\r\n\u0424\u0430\u0439\u043b\u043e\u0432\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430:\r\n\r\n\u041d\u043e\u0432\u0430\u044f \u043f\u0430\u043f\u043a\u0430\r\n\u251c\u2500\u2500\u2500img\r\n\u2502   \u251c\u2500\u2500\u2500kisa.jpg\r\n\u2502   \u2514\u2500\u2500\u2500kot.png\r\n\u251c\u2500\u2500\u2500index.html\r\n\u2514\u2500\u2500\u2500style.css\r\n\u041a\u043e\u0434 \u0432 index.html:\r\n\r\n\r\n<link rel=\"stylesheet\" href=\"style.css\">\r\n<img src=\"img/kisa.jpg\">\r\n<img src=\"img/kot.png\">\r\n\r\n\u041f\u0440\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0438 \u0437\u0430\u0434\u0430\u043d\u0438\u0439 \u0441 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435\u043c \u0444\u0430\u0439\u043b\u043e\u0432 - \u043a\u0430\u0440\u0442\u0438\u043d\u043e\u043a, \u0448\u0440\u0438\u0444\u0442\u043e\u0432, \u0432\u0435\u0431-\u0441\u0442\u0440\u0430\u043d\u0438\u0446, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0430\u0445\u043e\u0434\u044f\u0442\u0441\u044f \u043b\u043e\u043a\u0430\u043b\u044c\u043d\u043e (\u0442\u043e \u0435\u0441\u0442\u044c \u0443 \u0442\u0435\u0431\u044f \u043d\u0430 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0435), \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439 \u043e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u0441\u044b\u043b\u043a\u0438. \u041f\u043e\u0442\u043e\u043c\u0443 \u0447\u0442\u043e \u043f\u0440\u0438 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0435 \u043a\u043e\u0434\u0430 \u043d\u0430 \u0441\u0435\u0440\u0432\u0435\u0440, \u0441\u0441\u044b\u043b\u043a\u0438 \u0432\u0440\u043e\u0434\u0435 file:///C:/Users/admin/Desktop/\u041d\u043e\u0432\u0430\u044f%20\u043f\u0430\u043f\u043a\u0430/image.jpg \u043f\u0435\u0440\u0435\u0441\u0442\u0430\u043d\u0443\u0442 \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c.",
      "owner_id": 5
    }
  ],
  "courses_video": [],
  "courses_content": [
    {
      "id": 22,
      "object_id": 19,
      "content_type_id": 14,
      "module_id": 9,
      "order": 0
    },
    {
      "id": 24,
      "object_id": 20,
      "content_type_id": 14,
      "module_id": 10,
      "order": 0
    },
    {
      "id": 25,
      "object_id": 21,
      "content_type_id": 14,
      "module_id": 11,
      "order": 0
    },
    {
      "id": 27,
      "object_id": 22,
      "content_type_id": 14,
      "module_id": 11,
      "order": 2
    },
    {
      "id": 29,
      "object_id": 23,
      "content_type_id": 14,
      "module_id": 11,
      "order": 3
    },
    {
      "id": 30,
      "object_id": 5,
      "content_type_id": 10,
      "module_id": 11,
      "order": 4
    },
    {
      "id": 31,
      "object_id": 6,
      "content_type_id": 10,
      "module_id": 11,
      "order": 5
    },
    {
      "id": 32,
      "object_id": 7,
      "content_type_id": 10,
      "module_id": 11,
      "order": 6
    },
    {
      "id": 33,
      "object_id": 24,
      "content_type_id": 14,
      "module_id": 12,
      "order": 0
    },
    {
      "id": 34,
      "object_id": 8,
      "content_type_id": 10,
      "module_id": 12,
      "order": 1
    },
    {
      "id": 35,
      "object_id": 25,
      "content_type_id": 14,
      "module_id": 13,
      "order": 0
    },
    {
      "id": 36,
      "object_id": 9,
      "content_type_id": 10,
      "module_id": 13,
      "order": 1
    },
    {
      "id": 37,
      "object_id": 26,
      "content_type_id": 14,
      "module_id": 14,
      "order": 0
    }
  ],
  "courses_module": [
    {
      "id": 9,
      "title": "\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430, \u0442\u0435\u0433\u0438 \u0438 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u044b",
      "description": "\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438 HTML \u0441\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0438",
      "course_id": 10,
      "order": 0
    },
    {
      "id": 10,
      "title": "\u0411\u043b\u043e\u0447\u043d\u044b\u0435 \u0438 \u0441\u0442\u0440\u043e\u0447\u043d\u044b\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b",
      "description": "\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0442\u0438\u043f\u044b \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432",
      "course_id": 10,
      "order": 1
    },
    {
      "id": 11,
      "title": "\u0421\u043f\u0438\u0441\u043a\u0438",
      "description": "\u0422\u0435\u0433\u0438 \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0421\u043f\u0438\u0441\u043a\u043e\u0432. \u041d\u0443\u043c\u0435\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0438 \u043d\u0435\u043d\u0443\u043c\u0435\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a",
      "course_id": 10,
      "order": 2
    },
    {
      "id": 12,
      "title": "\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f",
      "description": "\u0422\u0435\u0433 \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439",
      "course_id": 10,
      "order": 3
    },
    {
      "id": 13,
      "title": "\u0422\u0430\u0431\u043b\u0438\u0446\u044b",
      "description": "\u0422\u0435\u0433 \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0442\u0430\u0431\u043b\u0438\u0446",
      "course_id": 10,
      "order": 4
    },
    {
      "id": 14,
      "title": "\u0421\u0441\u044b\u043b\u043a\u0438, \u044f\u043a\u043e\u0440\u044f \u0438 \u043a\u043b\u0430\u0441\u0441\u044b",
      "description": "\u041a\u0430\u043a \u0441\u043e\u0437\u0434\u0430\u0432\u0430\u0442\u044c \u0441\u0441\u044b\u043b\u043a\u0438 \u0438 \u0447\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u043a\u043b\u0430\u0441\u0441\u044b",
      "course_id": 10,
      "order": 5
    },
    {
      "id": 15,
      "title": "\u0421\u0438\u043d\u0442\u0430\u043a\u0441\u0438\u0441 \u0438 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 CSS",
      "description": "\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f CSS \u0438 \u043a\u0430\u043a \u0435\u0433\u043e \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435",
      "course_id": 11,
      "order": 0
    },
    {
      "id": 16,
      "title": "\u0421\u0442\u0438\u043b\u0438 \u0448\u0440\u0438\u0444\u0442\u0430 \u0438 \u0442\u0435\u043a\u0441\u0442\u0430",
      "description": "\u041a\u0430\u043a \u0438\u0437\u043c\u0435\u043d\u044f\u0442\u044c \u0448\u0440\u0438\u0444\u0442 \u0438 \u0442\u0435\u043a\u0441\u0442",
      "course_id": 11,
      "order": 1
    },
    {
      "id": 17,
      "title": "\u0421\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u0431\u043b\u043e\u043a\u043e\u0432",
      "description": "\u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0431\u043b\u043e\u043a\u043e\u0432",
      "course_id": 11,
      "order": 2
    },
    {
      "id": 18,
      "title": "\u0421\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u0438 \u0441\u0442\u0438\u043b\u0438 \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u044f \u0431\u043b\u043e\u043a\u043e\u0432",
      "description": "\u041e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435 \u0431\u043b\u043e\u043a\u043e\u0432",
      "course_id": 11,
      "order": 3
    },
    {
      "id": 19,
      "title": "\u0421\u0432\u043e\u0439\u0441\u0442\u0432\u043e BACKGROUND",
      "description": "\u041a\u0430\u043a \u0438\u0437\u043c\u0435\u043d\u044f\u0442\u044c \u0444\u043e\u043d",
      "course_id": 11,
      "order": 4
    },
    {
      "id": 20,
      "title": "\u0427\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u0411\u042d\u041c",
      "description": "\u041a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u0411\u042d\u041c (\u0411\u043b\u043e\u043a, \u042d\u043b\u0435\u043c\u0435\u043d\u0442, \u041c\u043e\u0434\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440)",
      "course_id": 11,
      "order": 5
    }
  ],
  "courses_course_students": [
    {
      "id": 31,
      "course_id": 10,
      "user_id": 5
    },
    {
      "id": 43,
      "course_id": 11,
      "user_id": 5
    }
  ]
}
    
    total_imported = 0
    
    with transaction.atomic():
        for table_name, records in data.items():
            if not records:
                continue
                
            # Ищем модель
            model = None
            for app in apps.get_app_configs():
                for m in app.get_models():
                    if m._meta.db_table == table_name:
                        model = m
                        break
                if model:
                    break
            
            if not model:
                print(f"⚠️ Модель для таблицы {table_name} не найдена, пропускаем")
                continue
            
            print(f"📦 Импортируем {table_name} ({len(records)} записей)...")
            
            batch = []
            for record in records:
                try:
                    # Очищаем None значения
                    clean_record = {k: v for k, v in record.items() if v is not None}
                    
                    # Создаем объект
                    obj = model(**clean_record)
                    batch.append(obj)
                    
                    # Вставляем пачками по 100
                    if len(batch) >= 100:
                        model.objects.bulk_create(batch, ignore_conflicts=True)
                        batch = []
                        
                except Exception as e:
                    print(f"   ⚠️ Ошибка в записи: {e}")
                    continue
            
            # Вставляем остатки
            if batch:
                model.objects.bulk_create(batch, ignore_conflicts=True)
            
            imported = len(records)
            total_imported += imported
            print(f"   ✅ Импортировано: {imported}")
    
    print(f"\n🎉 ИМПОРТ ЗАВЕРШЕН! Всего записей: {total_imported}")
    print("\n🔑 Следующие шаги:")
    print("1. Создайте суперюзера: python manage.py createsuperuser")
    print("2. Проверьте данные в админке")
    print("3. Проверьте работу сайта")

if __name__ == "__main__":
    import_data()
