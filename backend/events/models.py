from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Event(models.Model):
    creation_date = models.DateTimeField(default=timezone.now)
    date = models.DateTimeField()
    title = models.CharField(max_length=128)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='my_events')
    how_many_minutes = models.IntegerField(default=60)
    #type = ''

    def get_date_when_send_mail(self):
        return self.date - timedelta(minutes=self.how_many_minutes)
