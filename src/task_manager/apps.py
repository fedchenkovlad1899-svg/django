from django.apps import AppConfig


class TaskManagerConfig(AppConfig):
    default_app_config = 'django.db.models.BigAutoField'
    name = 'task_manager'
    verbose_name = 'МЕНЕДЖЕР ЗАДАЧ'

    def ready(self):
        import task_manager.signals