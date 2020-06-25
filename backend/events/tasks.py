from celery import shared_task
from django.core.mail import send_mail


@shared_task
def event_notify(*args, **kwargs):
    send_mail(
        'Subject here',
        'Here is the message.',
        'shvidkiy.dmitriy@gmail.com',
        ['shvidkiy.dmitriy@gmail.com'],
        fail_silently=False,
    )