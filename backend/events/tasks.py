from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def event_notify(email: str, title: str, minutes: int, **kwargs):
    send_mail(
        'Event Reminder',
        f'Event {title} will start in {minutes} minutes',
        settings.DEFAULT_MAIL,
        [email],
        fail_silently=False,
    )
