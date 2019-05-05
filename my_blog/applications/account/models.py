from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class CommonUser(AbstractUser):
    """
    Define CommonUser Fields
    """
    email_active = models.BooleanField(default=False)
    avatar_uri = models.CharField(max_length=256, null=True)

    class Meta:
        db_table = "BlogCommonUser"



