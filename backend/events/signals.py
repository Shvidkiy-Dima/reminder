from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event
from .tasks import event_notify


@receiver(post_save, sender=Event, dispatch_uid='send_mail')
def event_handler(sender, instance, **kwargs):
    email = instance.author.email
    date_when_send_mail = instance.get_date_when_send_mail()
    event_notify.delay()
