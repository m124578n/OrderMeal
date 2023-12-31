from django.shortcuts import render
from django.http import JsonResponse
from store.models import Store, StoreImage

from OrderMeal.utils import verify_jwt
# Create your views here.

@verify_jwt
def get_all_store(request, *args, **kwargs):
    stores = Store.objects.all()
    stores = stores.values_list("id", "name", "note")
    return JsonResponse({"status": 200, "stores": list(stores)})


@verify_jwt
def get_all_stores_images(request, *args, **kwargs):
    images = StoreImage.objects.all()
    images = images.values_list("store", "image_url")
    return JsonResponse({"status": 200, "images": list(images)})


def create_new_store(request):
    pass


def update_store_info(request):
    pass


def delete_store(request):
    pass


def get_all_store_menu(request):
    pass


def add_new_menu_to_store(request):
    pass


def update_menu(request):
    pass


def delete_menu(request):
    pass


def add_image_to_store(request):
    pass


def update_image(request):
    pass


def delete_image(request):
    pass
