
from django.urls import path,include
from task_manager.views import TasksView, HomeTemplateView, TasksView, UserListView, TaskFormView,CommentFormView,AttachmentsFormView,AttachmentsView
from .views import UserReportView


urlpatterns = [
    path('', TasksView.as_view(), name = "tasks"),
    path('home', HomeTemplateView.as_view(), name = "home"),
    path('tasks', TasksView.as_view(), name = "tasks"),
    path('users', UserListView.as_view(), name = "users"),
    path('users/<int:user_id>/', UserReportView.as_view(), name='user_report'),
    path('create',TaskFormView.as_view(), name = "create_task"),
    path('comment/create',CommentFormView.as_view(), name = "create_comment"),
    path("create_attachment", AttachmentsFormView.as_view(), name="create_attachment"),
    path("attachments", AttachmentsView.as_view(), name="attachments"),
    path("api/", include("task_manager.v1.urls")),


]
