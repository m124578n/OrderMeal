from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    context = {}
    
    return render(request, 'index.html', context)


def login(request):
    pass


def store(request):
    pass


def store_menu(request):
    pass


def group(request):
    pass
