# Generated by Django 5.0.1 on 2024-01-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_remove_task_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='photos',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]