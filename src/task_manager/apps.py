from django.apps import AppConfig


class TaskManagerConfig(AppConfig):
    default_app_config = 'django.db.models.BigAutoField'
    name = 'task_manager'
    verbose_name = 'МЕНЕДЖЕР ЗАДАЧ'

    # def ready(self):
    #
    #     from task_manager.signals import my_test_signal
    #
    #
    #     # post_save.connect(my_test_signal)