from django.shortcuts import render
from django.http import JsonResponse
from group.models import Group
from OrderMeal.units import verify_jwt
# Create your views here.

@verify_jwt
def get_all_groups_by_status(request, *args, **kwargs):
    status = request.GET.get("status")
    groups = Group.objects.filter(status=Group.Status[status])
    return JsonResponse({"status" : 200, "groups" : list(groups.values())})


def create_new_group(request):
    pass


def update_group(request):
    pass


def delete_group(request):
    pass


def get_all_group_member(request):
    pass


def add_new_member_to_group(request):
    pass


def update_group_member_info(request):
    pass


def delete_group_member(request):
    pass
