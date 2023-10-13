from django.db import models


class Tasks(models.Model):
    task_name = models.CharField(max_length=300)
    date_created = models.DateField(auto_now_add=True)
    date_deadline = models.DateTimeField()

    def __str__(self):
        return self.task_name
