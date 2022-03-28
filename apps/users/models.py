from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    USER_TYPE_MODERATOR = 1  # Администратор
    USER_TYPE_EMPLOYEE = 2  # Менеджер проекта
    USER_TYPE_EMPLOYER = 3  # Разработчик

    USER_TYPE = (
        (USER_TYPE_EMPLOYEE, "Администратор"),
        (USER_TYPE_EMPLOYER, "Менеджер проекта"),
        (USER_TYPE_MODERATOR, "Разработчик"),
    )

    id = models.UUIDField(primary_key=True, default=uuid4)
    username = models.EmailField(unique=True, db_index=True, verbose_name="Почта")
    role = models.PositiveSmallIntegerField(choices=USER_TYPE, default=USER_TYPE_MODERATOR, verbose_name="Роль")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def get_role_name(self):
        for item in self.USER_TYPE:
            if item[0] == self.role:
                return item[1]
        return None

    def __str__(self):
        return f"{self.username}"

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name} {self.second_name}"

    @staticmethod
    def get_user_by_email(email):
        return User.objects.get(email=email)
