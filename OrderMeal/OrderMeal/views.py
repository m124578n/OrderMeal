from django.shortcuts import render
from django.http import JsonResponse
import jwt


def index(request):
    context = {}
    return render(request, 'index.html', context)


def login_page(request):
    return render(request, 'login.html')


def store(request):
    pass


def store_menu(request):
    pass


def group(request):
    pass


def login_api(request):
    pass
