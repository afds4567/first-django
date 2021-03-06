# Generated by Django 3.2.12 on 2022-03-14 02:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_firstcategory_first_category_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address_category_1', models.CharField(max_length=5)),
                ('address_category_2', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Knowhow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('coverImageUrl', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='pro',
            name='id',
        ),
        migrations.AddField(
            model_name='pro',
            name='company_name',
            field=models.CharField(default='user.name', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pro',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pro',
            name='is_safe_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pro',
            name='pro_description',
            field=models.CharField(default='소개글이 없습니다', max_length=200),
        ),
        migrations.AddField(
            model_name='pro',
            name='pro_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pro',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterModelTable(
            name='pro',
            table='pro',
        ),
        migrations.AddField(
            model_name='pro',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.address'),
        ),
    ]
