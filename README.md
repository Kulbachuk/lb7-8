# Django & Flask ORM Publishing Project (Lab 7-8)

Навчальний проєкт з розробки веб-додатків на **Django** та **Flask** у межах Лабораторної роботи №7-8 з дисципліни «Програмування».

**Студент:** Кульбачук Даниїл Сергійович  
**Група:** ФІКб-1-24 (№4 у списку)  
**Спеціальність:** Кібербезпека та захист інформації  
**Університет:** Київський столичний університет імені Бориса Грінченка (2026)

---

## 📌 Огляд проєкту

Проєкт демонструє роботу з об'єктно-реляційним відображенням (**ORM**), механізмами міграцій баз даних, паттерном **Unit of Work / Active Record**, а також автоматизованим тестуванням (**PyTest**) та розрахунком покриття коду (**Coverage**).

### 📁 Структура каталогу

```text
Лр7-8/
├── django_project/          # Проєкт на фреймворку Django
│   ├── config/              # Налаштування Django (settings, urls)
│   ├── publishing/          # Додаток видавництва (models, views, admin)
│   │   ├── models.py        # ORM-моделі (Author, AuthorProfile, Book, Tag)
│   │   ├── tests.py         # PyTest-тести для Django
│   │   └── demo.py          # Скрипт демонстрації CRUD-операцій
│   ├── conftest.py          # PyTest фікстури для Django
│   ├── pytest.ini           # Конфігурація PyTest та DJANGO_SETTINGS_MODULE
│   └── manage.py
│
└── flask_project/           # Проєкт на фреймворку Flask
    ├── app.py               # Ініціалізація Flask, маршрути та Flask-Migrate
    ├── models.py            # ORM-моделі на Flask-SQLAlchemy
    ├── demo.py              # Скрипт перевірки Unit of Work (commit, rollback)
    ├── conftest.py          # PyTest фікстури для Flask (in-memory SQLite)
    └── test_app.py          # Автотести Flask (моделі, HTTP GET /, mock)
```

---

## ⚙️ Інсталяція та налаштування

### 1. Клонування репозиторію та створення віртуального середовища
```powershell
git clone <url-вашого-репозиторію>
cd Лр7-8

# Створення та активація venv (Windows)
python -m venv venv
.env\Scriptsctivate
```

### 2. Встановлення залежностей
```powershell
pip install -r requirements.txt
```

---

## 🚀 Запуск проєкту

### 🟢 Django Проєкт (`django_project`)

1. Перейдіть у папку проєкту:
   ```powershell
   cd django_project
   ```
2. Виконайте міграції бази даних:
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Запустіть тестовий ORM-скрипт:
   ```powershell
   python publishing/demo.py
   ```
4. Запустіть автотести з розрахунком покриття коду:
   ```powershell
   py -m pytest --cov=publishing
   ```

---

### 🔵 Flask Проєкт (`flask_project`)

1. Перейдіть у папку проєкту:
   ```powershell
   cd ../flask_project
   ```
2. Ініціалізуйте та застосуйте міграції Flask-Migrate (Alembic):
   ```powershell
   py -m flask --app app db init
   py -m flask --app app db migrate -m "Initial migration"
   py -m flask --app app db upgrade
   ```
3. Запустіть демо-скрипт перевірки транзакцій (Unit of Work):
   ```powershell
   py demo.py
   ```
4. Запустіть автотести з розрахунком покриття коду:
   ```powershell
   py -m pytest --cov=. --cov-report=term-missing
   ```

---

## 🧪 Результати тестування (PyTest Coverage)

- **Django**: 7 пройшло (**100% passed**), покриття моделей `publishing/models.py` становить **96–100%**.
- **Flask**: 3 пройшло (**100% passed**), покриття `models.py` — **96%**, `app.py` — **93%**.
