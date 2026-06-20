#
# from rest_framework.routers import DefaultRouter
#
# from task_manager.v1.views.task import TaskViewSet
#
# router = DefaultRouter()
# router.register('tasks', TaskViewSet, basename='tasks')
# urlpatterns = router.urls
#

from django.urls import path,include

urlpatterns = [
    path('tasks/', include("task_manager.v1.urls"), name='task_api'),
]