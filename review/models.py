from django.contrib.auth.models import User
from django.db import models


class Review(models.Model):
    owner = models.ForeignKey('auth.user', related_name='reviews', on_delete=models.CASCADE)
    whose = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.whose} - {self.owner}'
