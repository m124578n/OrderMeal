# Generated by Django 4.2.4 on 2023-10-11 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_store_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='catagory',
            new_name='category',
        ),
    ]
