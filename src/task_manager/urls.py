
from django.urls import path
from task_manager.views import tasks, home, tasks, users, create_task_form,create_comment_form,create_attachment,attachments
from .views import urequest


urlpatterns = [
    path('', tasks, name = "tasks"),
    path('home', home, name = "home"),
    path('tasks', tasks, name = "tasks"),
    path('users', users, name = "users"),
    path('users/<int:user_id>/', urequest, name='user_report'),
    path('create',create_task_form, name = "create_task"),
    path('comment/create',create_comment_form, name = "create_comment"),
    path("create_attachment", create_attachment, name="create_attachment"),
    path("attachments", attachments, name="attachments"),



]
