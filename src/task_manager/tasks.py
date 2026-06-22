from celery import shared_task
from account.models import User
from config.celery import app
from django.core.mail import send_mail


@shared_task
def add(x, y):
    import time
    time.sleep(60)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@app.task
def send(email):
    send_mail(
        "Приветствие",
        "С добрым утром!",
        'djangotester28@gmail.com',
        [email],
        fail_silently=False,
    )


@app.task
def send_sunrise_welcome():
    users = User.objects.exclude(email="")

    for user in users:
        if user.email:
            send(user.email)
            print(f"Пользователю {user.username} отправлено на {user.email}: С добрым утром!", flush=True)