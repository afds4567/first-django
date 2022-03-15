# Generated by Django 3.2.12 on 2022-03-15 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_knowhow_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProService',
            fields=[
                ('proservice_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_main', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='service',
            name='pro',
        ),
        migrations.AlterField(
            model_name='pro',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(default='Good', max_length=200)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('proservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.proservice')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.user')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.AddField(
            model_name='proservice',
            name='pro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.pro'),
        ),
        migrations.AddField(
            model_name='proservice',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.service'),
        ),
        migrations.AlterUniqueTogether(
            name='proservice',
            unique_together={('pro', 'service')},
        ),
    ]