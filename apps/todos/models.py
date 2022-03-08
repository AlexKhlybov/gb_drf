from django.db import models
from uuid import uuid4


class Project(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=128, verbose_name='Название')
    repo = models.URLField(verbose_name='Репозиторий')
    user = models.ManyToManyField('User', db_index=True, blank=True, verbose_name='Пользователи')
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
    
    def __str__(self):
        return f"{self.name}"

