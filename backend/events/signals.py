from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event
from .tasks import event_notify


@receiver(post_save, sender=Event, dispatch_uid='send_mail')
def event_handler(sender, instance, **kwargs):
    # TODO: Change from countdown to eta in future
    seconds_to_send_mail = instance.get_seconds_to_send_mail()

    event_notify.apply_async((instance.author.email, instance.title, instance.how_many_minutes),
                             countdown=seconds_to_send_mail)
