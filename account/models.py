from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    tasktext = models.TextField(max_length=200)
    create_at = models.DateTimeField(default=now, editable=False)
    is_active = models.BooleanField(default=True)
    ended_date = models.DateTimeField(default=now, editable=False)


    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering = ['pk']


