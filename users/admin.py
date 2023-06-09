from django.contrib import admin
from django.contrib.admin import ModelAdmin

from users.models import User


class UserAdmin(ModelAdmin):
    fields = ("username", "phone_number", "email", "password")
    list_display = ("username", "phone_number", "email", "password")


admin.site.register(User, UserAdmin)
