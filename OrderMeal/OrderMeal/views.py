from django.shortcuts import render
from django.http import JsonResponse
from staff.models import Staff

from OrderMeal.units import generate_jwt_token
import json


def index(request):
    context = {}
    return render(request, 'index.html', context)


def login_page(request):
    timeout = request.GET.get("timeout", None)
    context = {"timeout" : int(timeout)}
    return render(request, 'login.html', context)


def store(request):
    pass


def store_menu(request):
    pass


def group(request):
    pass


def login_api(request):
    body = request.body.decode("utf-8")
    body = json.loads(body)
    staff_id = body.get("userId", "")
    password = body.get("passwd", "")
    staff = Staff.objects.filter(staff_id=staff_id)
    if staff is None:
        return JsonResponse({"status" : 404})
    if staff[0].password != password:
        return JsonResponse({"status" : 402})
    token = generate_jwt_token(staff_id)
    return JsonResponse({"status" : 200 , "token" : token})
    

