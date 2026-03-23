
from django.urls import path
from task_manager.views import index,home,tasks,users

urlpatterns = [
    path('', index, name = "tasks"),
    path('home', home, name = "home"),
    path('tasks', tasks, name = "tasks"),
    path('users', users, name = "users"),
]
