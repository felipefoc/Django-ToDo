from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Youtube_file(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    

    def __str__(self):
        return '{}'.format(self.title)


