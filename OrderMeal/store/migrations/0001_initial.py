# Generated by Django 4.2.4 on 2023-10-11 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('describe', models.CharField(max_length=255)),
                ('note', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'store',
            },
        ),
        migrations.CreateModel(
            name='StoreMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=0, max_digits=7)),
                ('note', models.CharField(max_length=255)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
            options={
                'db_table': 'store_menu',
            },
        ),
        migrations.CreateModel(
            name='StoreImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=255)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
            options={
                'db_table': 'store_image',
            },
        ),
    ]
