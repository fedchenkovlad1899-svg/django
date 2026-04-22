import random
from django.core.management.base import BaseCommand
from account.models import User
from task_manager.models import Projects, Tasks, Tags, Comments
from faker import Faker

from task_manager.views import tasks
fake = Faker(['en_US',])

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        

        self.stdout.write("Генерация пользователей")
        users = [
            User(
            username=fake.unique.user_name(),
            email=fake.email()
            )
            for _ in range(100)
        ]
        User.objects.bulk_create(users)
        users = list(User.objects.all())

        self.stdout.write("Генерация проектов")
        projects = [
            Projects(name=fake.unique.company()[:64],
            description=fake.text()
            )
            for _ in range(10)
        ]
        Projects.objects.bulk_create(projects)
        projects = list(Projects.objects.all())

        self.stdout.write("Генерация тегов")

        tags = [
            Tags(
                name=fake.unique.word(),
            )
            for _ in range(10)]
        Tags.objects.bulk_create(tags)
        tags = list(Tags.objects.all())



        self.stdout.write("Генерация задач")
        batch_size = 10000
        for i in range(0, 10001, batch_size):
            tasks_to_create = [
                Tasks(
                    name=f"{fake.word()}_{i + j}_{random.randint(1, 999)}"[:64],
                    project=random.choice(projects),
                    assignee=random.choice(users),
                    status='created',
                    priority=3,
                ) for j in range(batch_size)
            ]


            created_tasks = Tasks.objects.bulk_create(tasks_to_create)





        self.stdout.write("Добавление комментариев")
        available_tasks = list(Tasks.objects.all()[:250])
        available_users = list(User.objects.all())

        comments = [
            Comments(
                task=random.choice(available_tasks),
                user=random.choice(available_users),
                message=fake.sentence()
            )
            for _ in range(250)
        ]
        Comments.objects.bulk_create(comments)

        self.stdout.write(self.style.SUCCESS('Данные сгенерированы!'))
