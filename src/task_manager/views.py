
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from task_manager.models import Tasks,Attachments,Comments

from account.models import User

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import transaction
from task_manager.forms import TaskForm,CommentForm,AttachmentsForm
from django.urls import reverse
from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models import F
from django.core.paginator import Paginator







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
    tasks_qs = Tasks.objects.task_optimization()
    paginator = Paginator(tasks_qs, 10)
    page_number = request.GET.get('page')
    page_objc = paginator.get_page(page_number)
    context = {'tasks': page_objc, 'page_obj': page_objc}

    return render(request, "tasks.html", context=context)


def urequest(request, user_id):


    user_qs = User.objects.prefetch_related('comments__task').filter(id=user_id)
    user = get_object_or_404(user_qs, id=user_id)

    context = {
        'user': user,
    }
    return render (request,"user_report.html", context=context)

def attachments(request):

    attachments_qs = Attachments.objects.all().order_by('id')
    paginator = Paginator(attachments_qs, 10)
    page_number = request.GET.get('page')
    page_objc = paginator.get_page(page_number)

    context = {
        'attachments': page_objc,
        'page_obj': page_objc
    }

    return render (request,"attachments.html", context=context)


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

def create_attachment(request):

    if request.method == "POST":

        form = AttachmentsForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()
            return HttpResponseRedirect(reverse("tasks"))
    else:
        form = AttachmentsForm()

    return render(request, "task_attachment.html", {"form": form})