from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from core.models import BaseModel

class CustomUserManager(UserManager):
    pass


class User(AbstractUser, BaseModel):
    email = models.EmailField(max_length=255, verbose_name="이메일", unique=True)
    username = models.CharField(max_length=30, verbose_name="이름", blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name="연락처", blank=True, null=True)


    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        verbose_name = "회원 관리"
        verbose_name_plural = "회원 관리"
