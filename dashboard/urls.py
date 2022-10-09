from django.urls import path

from .views import home, inquiry

urlpatterns = [
    path("", home, name="dashboard"),
    path("inquiry/", inquiry, name="inquiry"),
]
