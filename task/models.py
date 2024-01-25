from django.db import models
from category.models import Category


class YourModel(models.Model):
    PLACE_OF_SERVICE_CHOICES = [
        ('remote', 'Можно выполнить удалённо'),
        ('on_site', 'Нужно присутствие по адресу'),
    ]


class Task(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.SET_NULL, null=True, blank=False)

    start_at = models.DateTimeField(blank=True)
    finish_till = models.DateTimeField(blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    place_of_service = models.CharField(max_length=20, choices=YourModel.PLACE_OF_SERVICE_CHOICES, default='on_site',
                                        blank=False)
    address = models.CharField(max_length=300, blank=True if place_of_service != 'on_site' else False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title[:25]}...' if len(self.title) > 25 else self.title

    class Meta:
        ordering = ('created_at',)


class TaskImage(models.Model):
    image = models.ImageField(upload_to='images')
    task = models.ForeignKey(Task, related_name='images', on_delete=models.CASCADE)
