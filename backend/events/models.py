from datetime import timedelta
from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model


class Event(models.Model):
    creation_date = models.DateTimeField(default=now)
    date = models.DateTimeField()
    title = models.CharField(max_length=128)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='my_events')
    how_many_minutes = models.IntegerField(default=60)
    #type = ''

    def is_gone(self):
        return now() > self.date

    def get_seconds_to_send_mail(self):
        date_when_send = self.date - timedelta(minutes=self.how_many_minutes)
        return (date_when_send - now()).seconds if date_when_send > now() else 0
