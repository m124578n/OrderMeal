from django.urls import path
from group import views

urlpatterns = [
    path("", views.get_all_groups_by_status),
    path("user/", views.get_groups_by_user_id)
]
