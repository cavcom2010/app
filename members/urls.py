from django.urls import path
from .models import members

app_name = "members"

urlpatterns = [
    path("", views.index , name="members:index"),
]