
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from task_manager.models import Tasks

from account.models import User

from django.http import HttpResponseRedirect
from task_manager.forms import TaskForm,CommentForm
from django.urls import reverse
from django.core.signals import request_finished
from django.dispatch import receiver









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

        'users': users

    }

    return render(request, "users.html",context=context)


# @receiver(request_finished)
# def...
# print("Request finished!")


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



def create_task_form(request):

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():

            # Tasks.objects.create(
            #     name=request.POST["name"],
            #     priority=request.POST["priority"]
            # )

            # Tasks.objects.create(
            #     name=request.cleaned_data.get("name"),
            #     priority=request.cleaned_data.get("priority")
            # )

            form.save()
            return HttpResponseRedirect(reverse("tasks"))
    else:
        form = TaskForm()

    return render(request, "task_form.html", {"form": form})





def create_comment_form(request):

    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():



            form.save()
            return HttpResponseRedirect(reverse("tasks"))
    else:
        form = CommentForm()

    return render(request, "comment_form.html", {"form": form})