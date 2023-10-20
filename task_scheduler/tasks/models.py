from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=300)
    date_created = models.DateField(auto_now_add=True)
    date_deadline = models.DateTimeField()

    def __str__(self):
        return self.task_name
