from django.db import models

# Create your models here.

from django.conf import settings


class Follower(models.Model):
    """ Модель подписчиков
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner'
    )
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscribers'
    )

