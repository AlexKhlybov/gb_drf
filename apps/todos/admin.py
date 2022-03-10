from dataclasses import field

from django.contrib import admin
from import_export import resources

from apps.todos.models import Project, Todo

admin.site.register(Project)
admin.site.register(Todo)


class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project
        fields = "__all__"


class TodoResource(resources.ModelResource):
    class Meta:
        model = Todo
        fields = "__all__"
