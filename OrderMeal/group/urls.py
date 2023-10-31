from django.urls import path
from group import views

urlpatterns = [
    path("", views.get_all_group)
]
