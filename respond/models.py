from django.db import models
from task.models import Task


class Respond(models.Model):
    owner = models.ForeignKey('auth.User', related_name='responds', on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name='responds', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'task']

    def __str__(self):
        return f'{self.task}'




