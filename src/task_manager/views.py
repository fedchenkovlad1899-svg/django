from django.shortcuts import render, get_object_or_404


from django.http import HttpResponse
from task_manager.models import Tasks


from account.models import User


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

        'users': users #Tasks.objects.filter(assignee_id=2),

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

        'tasks': Tasks.objects.select_related("assignee").prefetch_related("tags","comments").all()

    }

    return render(request, "tasks.html",context=context)


def urequest(request, user_id):


    user_qs = User.objects.prefetch_related('comments__task').filter(id=user_id)
    user = get_object_or_404(user_qs, id=user_id)

    context = {
        'user': user,
    }
    return render (request,"user_report.html", context=context)