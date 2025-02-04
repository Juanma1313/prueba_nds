from django.db import models
from django.contrib.auth.models import AbstractUser


# Data Model for the task manager user to allow for future additional fields
class Task_mgr_User(AbstractUser):
    job_title = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username
