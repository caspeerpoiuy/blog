from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class CommonUser(models.Model):
    """
    Define CommonUser Fields
    """
    username = models.CharField(max_length=64, unique=True, db_index=True, null=False)
    password = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=128, null=True)
    mobile = models.CharField(max_length=32, null=True)
    nick_name = models.CharField(max_length=32, default=username)
    avatar_url = models.CharField(max_length=256, default=None)
    created_time = models.DateTimeField('创建时间', default=now)
    active_time = models.DateTimeField('活跃时间', default=now)

    class Meta:
        db_table = "CommonUser"
