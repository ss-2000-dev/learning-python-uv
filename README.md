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
