from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("view-page/<str:pk>/", views.pages, name="pages")
]
