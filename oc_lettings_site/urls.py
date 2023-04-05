from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
]

# Utiliser les regex pour réduire
# Le linting
# Créer 2 apps au lieu d'une seule
# Docker regarder la doc
# Circle CI
