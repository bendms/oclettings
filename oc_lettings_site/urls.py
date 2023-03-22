from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", views.lettings_index, name="lettings_index"),
    path("lettings/<int:letting_id>/", views.letting, name="letting"),
    path("profiles/", views.profiles_index, name="profiles_index"),
    path("profiles/<str:username>/", views.profile, name="profile"),
    path("admin/", admin.site.urls),
]

# Utiliser les regex pour réduire
# Le linting
# Créer 2 apps au lieu d'une seule
# Docker regarder la doc
# Circle CI
