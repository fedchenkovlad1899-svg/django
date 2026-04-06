
from django.urls import path
from task_manager.views import tasks,home,tasks,users

urlpatterns = [
    path('', tasks, name = "tasks"),
    path('home', home, name = "home"),
    path('tasks', tasks, name = "tasks"),
    path('users', users, name = "users"),
]
