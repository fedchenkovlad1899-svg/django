from django.db.models.signals import post_save
from django.dispatch import receiver
from task_manager.models import Tasks, Comments
from account.models import User


@receiver(post_save, sender=Tasks)
def my_test_signal(sender,instance,created, **kwargs):
    user = User.objects.get(id=1)
    instance.assignee = user
    # instance.save()


# @receiver(post_save, sender=Tasks)
# def create_task_comment_signal(sender, instance, created, **kwargs):
#     if created:
#         Comments.objects.create(
#             task=instance,
#             user=instance.assignee,
#             message="Task created"
#         )