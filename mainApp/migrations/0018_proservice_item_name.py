# Generated by Django 3.2.12 on 2022-03-16 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0017_alter_knowhow_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='proservice',
            name='item_name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
