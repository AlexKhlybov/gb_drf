# Generated by Django 3.2.12 on 2022-03-09 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('repo', models.URLField(verbose_name='Репозиторий')),
                ('user', models.ManyToManyField(blank=True, db_index=True, to=settings.AUTH_USER_MODEL, verbose_name='Пользователи')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.project', verbose_name='Проект')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
            },
        ),
    ]
