from django.shortcuts import render
from django.http import JsonResponse
from group.models import Group, GroupMember
from OrderMeal.utils import verify_jwt
# Create your views here.

@verify_jwt
def get_all_groups_by_status(request, *args, **kwargs):
    status = request.GET.get("status")
    user_id = kwargs["user_id"]
    # 排除自己已經有購買的團
    # 找到自己所在的團
    group_member = GroupMember.objects.only("group__id").filter(group_member__staff_id=user_id, group__status=Group.Status.START)
    exclude_groups = list(group_member.values_list("group__id"))[0]
    # 搜尋條件外加排除條件
    groups = Group.objects.filter(status=Group.Status[status]).exclude(id__in = exclude_groups)
    # 輸出需要顯示的欄位
    groups = groups.values_list("id", "status", "note")
    return JsonResponse({"status" : 200, "groups" : list(groups)})

@verify_jwt
def get_groups_by_user_id(request, *args, **kwargs):
    user_id = kwargs["user_id"]
    groups = GroupMember.objects.only("group__id", "group__status", "group__note").filter(group_member__staff_id=user_id, group__status=Group.Status.START)
    groups = groups.values_list("group__id", "group__status", "group__note")
    return JsonResponse({"status" : 200, "groups" : list(groups)})


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
