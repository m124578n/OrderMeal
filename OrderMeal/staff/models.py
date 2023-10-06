from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=255)
    staff_id = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        db_table = 'staff'
