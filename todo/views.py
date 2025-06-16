from django.shortcuts import render

# Temporary Task
TASKS = [
    {'id': 1, 'title': 'Buy groceries'},
    {'id': 2, 'title': 'Walk the dog'},
    {'id': 3, 'title': 'Study Django'},
]

def todo_list(request):
    return render(request, 'todo/todo_list.html', {'tasks': TASKS})
