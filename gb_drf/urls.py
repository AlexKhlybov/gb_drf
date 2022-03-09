from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.users.views import UserModelViewSet
from apps.todos.views import ProjectModelViewSet, TodoModelViewSet

router = DefaultRouter()
router.register("users", UserModelViewSet)
router.register("project", ProjectModelViewSet)
router.register("todos", TodoModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
]
