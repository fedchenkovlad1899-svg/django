
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.views.generic import TemplateView,DetailView
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
from django.views.decorators.cache import cache_page
from django.core.cache import caches
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy






# def tasks(request):
#
#
#     return render(request,"home.html")

# def home(request):
#     return render(request, "home.html")
class HomeTemplateView(TemplateView):
    template_name = "home.html"

# def users(request):
#     context = {
#         "users": User.objects.all(),
#     }
#     return render(request, "users.html", context=context)

class UserListView(ListView):
    model = User
    template_name = "users.html"
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context["users"] = self.queryset
        return context






# @receiver(request_finished)
# def...
# print("Request finished!")

# @cache_page(1800,cache='default')
# def tasks(request):
#
#
#     tasks_qs = Tasks.objects.task_optimization()
#     paginator = Paginator(tasks_qs, 10)
#     page_number = request.GET.get('page')
#     page_objc = paginator.get_page(page_number)
#     context = {'tasks': page_objc, 'page_obj': page_objc}
#
#     return render(request, "tasks.html", context=context)


class TasksView(ListView):
    template_name = "tasks.html"
    model = Tasks
    paginate_by = 50
    paginator_class = Paginator
    queryset = Tasks.objects.task_optimization()

    def get_context_data(self, **kwargs):
        context = super(TasksView, self).get_context_data(**kwargs)
        page_number = self.request.GET.get(self.page_kwarg)
        paginator = self.paginator_class(self.queryset,self.paginate_by)
        context["tasks"] = paginator.get_page(page_number)
        context["page_obj"] = paginator.get_page(page_number)
        return context


# def urequest(request, user_id):
#
#
#     user_qs = User.objects.prefetch_related('comments__task').filter(id=user_id)
#     user = get_object_or_404(user_qs, id=user_id)
#
#     context = {
#         'user': user,
#     }
#     return render (request,"user_report.html", context=context)



class UserReportView(DetailView):
    model = User
    template_name = "user_report.html"
    context_object_name = "user"
    pk_url_kwarg = "user_id"

    def get_queryset(self):
        return User.objects.prefetch_related('comments__task')



# def attachments(request):
#
#     attachments_qs = Attachments.objects.all().order_by('id')
#     paginator = Paginator(attachments_qs, 10)
#     page_number = request.GET.get('page')
#     page_objc = paginator.get_page(page_number)
#
#     context = {
#         'attachments': page_objc,
#         'page_obj': page_objc
#     }
#
#     return render (request,"attachments.html", context=context)

class AttachmentsView(ListView):
    template_name = "attachments.html"
    model = Attachments
    context_object_name = "attachment"
    paginate_by = 10
    paginator_class = Paginator
    queryset = Attachments.objects.prefetch_related("task").all()

    def get_context_data(self, **kwargs):
        context = super(AttachmentsView, self).get_context_data(**kwargs)
        page_number = self.request.GET.get("page")
        paginator = self.paginator_class(self.queryset, self.paginate_by)
        context["attachments"] = paginator.get_page(page_number)
        context["page_obj"] = paginator.get_page(page_number)
        return context


# def create_task_form(request):
#
#     if request.method == "POST":
#
#         form = TaskForm(request.POST)
#
#         if form.is_valid():
#
#             # Tasks.objects.create(
#             #     name=request.POST["name"],
#             #     priority=request.POST["priority"]
#             # )
#
#             # Tasks.objects.create(
#             #     name=request.cleaned_data.get("name"),
#             #     priority=request.cleaned_data.get("priority")
#             # )
#
#             form.save()
#             # caches["default"].clear()
#             return HttpResponseRedirect(reverse("tasks"))
#     else:
#         form = TaskForm()
#
#     return render(request, "task_form.html", {"form": form})

class TaskFormView(CreateView):
    template_name = "task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks")




# def create_comment_form(request):
#
#     if request.method == "POST":
#
#         form = CommentForm(request.POST)
#
#         if form.is_valid():
#
#
#
#             form.save()
#             return HttpResponseRedirect(reverse("tasks"))
#     else:
#         form = CommentForm()
#
#     return render(request, "comment_form.html", {"form": form})

class CommentFormView(CreateView):
    template_name = "comment_form.html"
    form_class = CommentForm
    success_url = reverse_lazy("tasks")

# def create_attachment(request):
#
#     if request.method == "POST":
#
#         form = AttachmentsForm(request.POST,request.FILES)
#
#         if form.is_valid():
#
#             form.save()
#             return HttpResponseRedirect(reverse("tasks"))
#     else:
#         form = AttachmentsForm()
#
#     return render(request, "task_attachment.html", {"form": form})

class AttachmentsFormView(CreateView):
    template_name = "task_attachment.html"
    model = Attachments
    form_class = AttachmentsForm
    success_url = reverse_lazy("tasks")