# Generated by Django 5.0.1 on 2024-01-22 13:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('photos', models.ImageField(blank=True, upload_to='images')),
                ('start_at', models.DateTimeField(blank=True)),
                ('finish_till', models.DateTimeField(blank=True)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('place_of_service', models.CharField(blank=True, choices=[('remote', 'Can be done remotely'), ('on_site', 'Required to be present at the address')], max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='category.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='TaskImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='task.task')),
            ],
        ),
    ]
