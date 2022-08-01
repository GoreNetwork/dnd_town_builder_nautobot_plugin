"""Urls for dnd_town_builder_nautobot_plugin."""

from django.urls import path

from dnd_town_builder_nautobot_plugin import views

urlpatterns = [
    # path('random/', views.RandomAnimalView.as_view(), name='random_animal'),
    path("built_city", views.built_city, name = "built_city"),
    path("build_city", views.build_city, name = "build_city"),
]