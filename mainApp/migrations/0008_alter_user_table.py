# Generated by Django 3.2.12 on 2022-03-14 02:39

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False # **<<< HERE**

    initial = True
    dependencies = [
        ('mainApp', '0007_auto_20220314_1138'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
