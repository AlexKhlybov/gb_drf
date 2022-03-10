from ast import mod
from uuid import uuid4

from django.db import models
from django.db.models.deletion import CASCADE

from apps.users.models import User


class Project(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=128, verbose_name="Название")
    repo = models.URLField(verbose_name="Репозиторий")
    user = models.ManyToManyField(User, db_index=True, blank=True, verbose_name="Пользователи")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return f"{self.name}"


class Todo(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=128, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")

    project = models.ForeignKey(Project, on_delete=CASCADE, verbose_name="Проект")
    user = models.ForeignKey(User, on_delete=CASCADE, verbose_name="Пользователь")

    is_active = models.BooleanField(verbose_name="Активно", default=True)
    create_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    def __str__(self):
        return f"{self.name} ({self.project})"
