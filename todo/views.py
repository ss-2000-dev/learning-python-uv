from django.shortcuts import render, redirect
from django.utils.html import escape
from .models import Task

# Temporary Task
# TASKS = [
#     {'id': 1, 'title': 'Buy apples'},
#     {'id': 2, 'title': 'Walk the dog'},
#     {'id': 3, 'title': 'Study Django'},
# ]


def todo_list(request):
    if request.method == "POST":
        # strip() removes leading and trailing whitespace
        title = request.POST.get("task", "").strip() 
        if title:
            # new_task = {
            #     'id': len(TASKS) + 1, 
            #     'title': escape(title) # escape() prevents XSS attacks by escaping HTML characters
            #     }
            # TASKS.append(new_task)
            Task.objects.create(title=title) 
        return redirect('/') # POST/Redirect pattern to avoid resubmission

    tasks = Task.objects.all() 
    return render(request, 'todo/todo_list.html', {'tasks': tasks})


def delete_task(request, task_id):
    if request.method == 'POST':
        # if 0 <= task_id < len(TASKS):
            # del TASKS[task_id]
        pass
    return redirect('todo_list')


def edit_task(request, task_id):
    # if not (0 <= task_id < len(TASKS)):
    #     return redirect("todo_list")
    
    # if request.method == "POST":
    #     new_title = request.POST.get("title")
    #     if new_title:
    #         TASKS[task_id]["title"] = new_title
    #     return redirect("todo_list")
    
    # task = TASKS[task_id]
    # return render(request, "todo/edit_task.html", {"task": task, "task_id": task_id})
    return redirect("todo_list")