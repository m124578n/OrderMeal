from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=255)
    describe = models.CharField(max_length=255)
    note = models.CharField(max_length=255)

    class Meta:
        db_table = 'store'


class StoreImage(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'store_image'


class StoreMenu(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=0)
    note = models.CharField(max_length=255)

    class Meta:
        db_table = 'store_menu'
