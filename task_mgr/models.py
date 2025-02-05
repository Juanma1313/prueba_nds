from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone


# Data Model for the task manager user to allow for future additional fields
class Task_mgr_User(AbstractUser):
    job_title = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username


STATUS = ((0, "Pending"), (1, "Compleated"), (2, "Cancelled"))
PRIORITY = ((0, "No"), (1, "Low"), (2, "Normal"), (3, "Hi"), (4, "unavoidable"))


# Data model for the task manager task
class Task_mgr_Task(models.Model):
    title = models.CharField(max_length=80)
    details = models.TextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="tasks")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    starts_on = models.DateTimeField()
    ends_on = models.DateTimeField()
    priority = models.IntegerField(choices=PRIORITY, default=0)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ["starts_on"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.starts_on is None:
            self.starts_on = timezone.now()

        if self.ends_on is None:
            self.start_on = timezone.now()

        if self.ends_on < self.starts_on:
            self.ends_on = self.starts_on

        super().save(*args, **kwargs)
