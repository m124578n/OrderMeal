from django.contrib import admin
from .models import Store, StoreImage, StoreMenu

# Register your models here.
admin.site.register(Store)
admin.site.register(StoreImage)
admin.site.register(StoreMenu)
