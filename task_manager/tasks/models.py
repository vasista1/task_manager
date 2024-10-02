from django.db import models

# Create your models here.

status_choices = (
    ('to_do','To do'),
    ('in_progress','In  progress'),
    ('done','Done'),
    ('archive','Archive'),
)

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    status = models.CharField(choices=status_choices, max_length=50)
    dead_line = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)