# Generated by Django 3.2.12 on 2022-03-14 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20220313_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('banner_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_url', models.URLField()),
            ],
            options={
                'db_table': 'banners',
            },
        ),
        migrations.CreateModel(
            name='Pro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-request_count']},
        ),
        migrations.AlterField(
            model_name='service',
            name='service_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='pro',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.service'),
        ),
        migrations.AddField(
            model_name='pro',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainApp.user'),
        ),
    ]
