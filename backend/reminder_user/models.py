from django.contrib.auth.models import AbstractUser
from django.db import models


class ReminderUser(AbstractUser):
    email = models.EmailField(blank=False, null=False)
