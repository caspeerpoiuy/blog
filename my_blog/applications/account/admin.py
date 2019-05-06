from django.contrib import admin
from .models import CommonUser


class CommonUserAdmin(admin.ModelAdmin):
    list_display = ["username","last_login","date_joined"]
    search_fields = ["username", "email"]




admin.site.register(CommonUser, CommonUserAdmin)
