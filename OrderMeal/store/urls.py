from django.urls import path
from store import views

urlpatterns = [
    path("", views.get_all_store),
    path("images/", views.get_all_stores_images)
]
