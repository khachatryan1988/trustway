# Trust Way — Django + Jinja2 Website

Проект сайта Trust Way на Django с Jinja2-шаблонами, мультиязычностью HY/RU/EN и админкой для редактирования контента.

## Возможности

- Главная страница
- Страница "О нас"
- Страница "Услуги"
- Страница "Контакты"
- Страница "Privacy Policy"
- Переключение языков HY / RU / EN
- Django Admin для управления контентом
- Контактная форма с сохранением заявок в админке
- Редактируемые:
    - тексты страниц
    - услуги
    - статистика
    - маршруты на карте
    - партнёры
    - ценности компании
    - шаги работы
    - footer links
    - контакты сайта

---

## Стек

- Python
- Django
- Jinja2
- SQLite
- HTML / CSS / JS
- Django Admin

---

## Структура проекта

```text
trustway_project_admin/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── trustway_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── i18n.py
│   ├── jinja2.py
│   ├── context_processors.py
│   │
│   ├── migrations/
│   │
│   ├── management/
│   │   └── commands/
│   │       └── seed_trustway.py
│   │
│   ├── jinja2/
│   │   └── core/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── about.html
│   │       ├── services.html
│   │       ├── contacts.html
│   │       └── privacy.html
│   │
│   └── static/
│       ├── css/
│       │   └── main.css
│       ├── js/
│       │   └── app.js
│       └── img/
```

## Быстрый запуск

```powershell
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations core
python manage.py migrate
python manage.py seed_trustway
python manage.py createsuperuser
python manage.py runserver
```