# transfer_data.py
import os
import sys
import django
import json
import sqlite3
from pathlib import Path

# Добавляем проект в sys.path
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'education.settings')
django.setup()

from django.core.management import execute_from_command_line

def export_local_data():
    """Экспорт данных с обработкой проблемных символов"""
    print("🚀 Начинаем экспорт данных...")
    
    # Способ 1: Через SQLite напрямую (обходит проблемы Django)
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Получаем все таблицы
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tables = [row[0] for row in cursor.fetchall()]
    
    all_data = {}
    for table in tables:
        try:
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            
            # Конвертируем в JSON-совместимый формат
            table_data = []
            for row in rows:
                row_dict = {}
                for idx, col in enumerate(cursor.description):
                    value = row[idx]
                    
                    # Обрабатываем проблемные символы и типы данных
                    if isinstance(value, bytes):
                        value = value.decode('utf-8', errors='replace')
                    elif isinstance(value, str):
                        # Заменяем проблемные символы
                        value = value.replace('\u2003', ' ').replace('\u2002', ' ')
                    elif isinstance(value, (int, float, type(None))):
                        pass  # Оставляем как есть
                    else:
                        value = str(value)
                    
                    row_dict[col[0]] = value
                table_data.append(row_dict)
            
            all_data[table] = table_data
            print(f"✅ Таблица {table}: {len(table_data)} записей")
            
        except Exception as e:
            print(f"⚠️ Ошибка в таблице {table}: {e}")
    
    conn.close()
    
    # Сохраняем в файл
    with open('data_export.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n📊 ВСЕГО экспортировано: {sum(len(v) for v in all_data.values())} записей")
    print("📁 Файл создан: data_export.json")
    
    # Создаем команду для импорта
    create_import_command(all_data)

def create_import_command(data):
    """Создает Python скрипт для импорта на Render"""
    import_script = '''# auto_import.py - запустить на Render
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
    data = ''' + json.dumps(data, indent=2) + '''
    
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
    
    print(f"\\n🎉 ИМПОРТ ЗАВЕРШЕН! Всего записей: {total_imported}")
    print("\\n🔑 Следующие шаги:")
    print("1. Создайте суперюзера: python manage.py createsuperuser")
    print("2. Проверьте данные в админке")
    print("3. Проверьте работу сайта")

if __name__ == "__main__":
    import_data()
'''
    
    with open('auto_import.py', 'w', encoding='utf-8') as f:
        f.write(import_script)
    
    print("\n📄 Создан скрипт для импорта: auto_import.py")
    print("\n📋 ИНСТРУКЦИЯ ДЛЯ RENDER:")
    print("1. Закоммитьте auto_import.py в Git")
    print("2. На Render откройте Shell")
    print("3. Выполните: python auto_import.py")
    print("4. Выполните: python manage.py createsuperuser")

if __name__ == "__main__":
    export_local_data()