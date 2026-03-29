from django.shortcuts import render

from django.http import HttpResponse
from task_manager.models import Tasks


def tasks(request):

    return render(request,"home.html")

def home(request):
    return render(request, "home.html")
def users(request):
    users = [
        {"name": "Alice", "age": 25,"photo":"1.jpg"},
        {"name": "Bob", "age": 30,"photo":"2.jpg"},
        {"name": "Charlie", "age": 28,"photo":"3.jpg"},
        {"name": "Diana", "age": 22,"photo":"4.jpg"}
    ]
    context = {

        'users': users,

    }

    return render(request, "users.html",context=context)

def tasks(request):
    tasks = [
        {"task_name": "Fix login bug", "status": "in progress", "priority": "high"},
        {"task_name": "Create navbar", "status": "done", "priority": "medium"},
        {"task_name": "Write tests", "status": "todo", "priority": "high"},
        {"task_name": "Update documentation", "status": "todo", "priority": "low"},
        {"task_name": "Deploy project", "status": "in progress", "priority": "medium"}
    ]
    context = {

        'tasks': Tasks.objects.all()

    }

    return render(request, "tasks.html",context=context)