from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class CommonUser(AbstractUser):
    """
    Define CommonUser Fields
    """
    email_active = models.BooleanField(default=False)
    avatar_uri = models.URLField(max_length=256, null=True)

    class Meta:
        db_table = "BlogCommonUser"


class UserCode(models.Model):

    code = models.CharField(max_length=64, null=False, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "BlogUserCode"