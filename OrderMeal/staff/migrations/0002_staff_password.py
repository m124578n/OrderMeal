# Generated by Django 4.2.4 on 2023-10-30 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='password',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
    ]
