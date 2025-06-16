from django.shortcuts import render, redirect
from django.utils.html import escape

# Temporary Task
TASKS = [
    {'id': 1, 'title': 'Buy groceries'},
    {'id': 2, 'title': 'Walk the dog'},
    {'id': 3, 'title': 'Study Django'},
]


def todo_list(request):
    if request.method == "POST":
        # strip() removes leading and trailing whitespace
        title = request.POST.get("task", "").strip() 
        if title:
            new_task = {
                'id': len(TASKS) + 1, 
                'title': escape(title) # escape() prevents XSS attacks by escaping HTML characters
                }
            TASKS.append(new_task)
        return redirect('/') # POST/Redirect pattern to avoid resubmission

    return render(request, 'todo/todo_list.html', {'tasks': TASKS})


def delete_task(request, task_id):
    if request.method == 'POST':
        if 0 <= task_id < len(TASKS):
            del TASKS[task_id]
    return redirect('todo_list')