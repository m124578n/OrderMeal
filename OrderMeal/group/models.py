from django.db import models
from staff.models import Staff
from store.models import Store, StoreMenu
# Create your models here.

class Group(models.Model):
    class Status(models.IntegerChoices):
        START = 0
        FULL = 1
        TIMESUP = 2
        END = 3
        CANCEL = 4
    group_owner = models.ForeignKey(Staff, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices)
    note = models.CharField(max_length=255)

    class Meta:
        db_table = 'group'


class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    group_member = models.ForeignKey(Staff, on_delete=models.CASCADE)
    picked_item = models.ForeignKey(StoreMenu, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=7, decimal_places=0)
    item_quantity = models.DecimalField(max_digits=3, decimal_places=0)
    is_pay = models.BooleanField(default=False)

    class Meta:
        db_table = 'group_member'
