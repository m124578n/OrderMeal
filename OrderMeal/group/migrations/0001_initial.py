# Generated by Django 4.2.4 on 2023-10-11 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Start'), (1, 'Full'), (2, 'Timesup'), (3, 'End'), (4, 'Cancel')])),
                ('note', models.CharField(max_length=255)),
                ('group_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('item_price', models.DecimalField(decimal_places=0, max_digits=7)),
                ('item_quantity', models.DecimalField(decimal_places=0, max_digits=3)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.group')),
                ('group_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
                ('picked_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.storemenu')),
            ],
            options={
                'db_table': 'group_member',
            },
        ),
    ]
