
from django.urls import path
from task_manager.views import tasks,home,tasks,users
from .views import urequest
urlpatterns = [
    path('', tasks, name = "tasks"),
    path('home', home, name = "home"),
    path('tasks', tasks, name = "tasks"),
    path('users', users, name = "users"),
    path('users/<int:user_id>/', urequest, name='user_report'),


]
