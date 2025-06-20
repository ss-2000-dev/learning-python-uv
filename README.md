## Learning Python uv Django

#### 2025/06/15

- setup uv

  - setup : `uv init learning-python-uv`
  - confirom uv setup : `uv run main.py`

- First Step (Show Hello World)

  - Add Pacakge : `uv add django`
  - create files
  - Run Server : `uv run python manage.py runserver`

- Start Create Todo App
  - show sample task

#### 2025/06/16

- Add Item
  - Create Input Form
  - Add Item usgin POST method
- Delete Item
- Edit Item
- Learning MVC, MTV

#### 2025/06/17

- Dockerize Todo app
  - `docker build -t uv-django-todo .`
  - `docker run --name uv-django-todo-container -p 8080:8080 uv-django-todo`
- Learning uv sync command
- Implement Docker Compose watch for hot reloading
  - `docker compose watch`

#### 2025/06/18

- Add MySQL Service
- Test Migration(log)
  - add command (`/app/.venv/bin/python manage.py migrate`)in compose.yaml
- Learn compose commad → not yet maybe tommorow

```
uv-django-todo-containner  | Operations to perform:
uv-django-todo-containner  |   Apply all migrations: admin, auth, contenttypes, sessions
uv-django-todo-containner  | Running migrations:
uv-django-todo-containner  |   Applying contenttypes.0001_initial... OK
uv-django-todo-containner  |   Applying auth.0001_initial... OK
uv-django-todo-containner  |   Applying admin.0001_initial... OK
uv-django-todo-containner  |   Applying admin.0002_logentry_remove_auto_add... OK
uv-django-todo-containner  |   Applying admin.0003_logentry_add_action_flag_choices... OK
uv-django-todo-containner  |   Applying contenttypes.0002_remove_content_type_name... OK
uv-django-todo-containner  |   Applying auth.0002_alter_permission_name_max_length... OK
uv-django-todo-containner  |   Applying auth.0003_alter_user_email_max_length... OK
uv-django-todo-containner  |   Applying auth.0004_alter_user_username_opts... OK
uv-django-todo-containner  |   Applying auth.0005_alter_user_last_login_null... OK
uv-django-todo-containner  |   Applying auth.0006_require_contenttypes_0002... OK
uv-django-todo-containner  |   Applying auth.0007_alter_validators_add_error_messages... OK
uv-django-todo-containner  |   Applying auth.0008_alter_user_username_max_length... OK
uv-django-todo-containner  |   Applying auth.0009_alter_user_last_name_max_length... OK
uv-django-todo-containner  |   Applying auth.0010_alter_group_name_max_length... OK
uv-django-todo-containner  |   Applying auth.0011_update_proxy_permissions... OK
uv-django-todo-containner  |   Applying auth.0012_alter_user_first_name_max_length... OK
uv-django-todo-containner  |   Applying sessions.0001_initial... OK
uv-django-todo-containner exited with code 0
```

#### 2025/06/19

- Learning Docker Command

#### 2025/06/20 night

- Define Task Model and Migration
  - `/app/.venv/bin/python manage.py makemigrations todo `
  - `/app/.venv/bin/python manage.py migrate`

```
uv-django-todo-containner  | Migrations for 'todo':
uv-django-todo-containner  |   todo/migrations/0001_initial.py
uv-django-todo-containner  |     + Create model Task
uv-django-todo-containner exited with code 0
```

- What mean "Migration" → 　 Not yet
