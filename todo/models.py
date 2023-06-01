import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class Task(models.Model):

    STATUS = (
    ('open','OPEN'),
    ('working', 'WORKING'),
    ('done','DONE'),
    ('overdue','OVERDUE'),
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    due_date = models.DateTimeField(blank=True)
    tags = models.ManyToManyField(Tag,blank=True)
    status =  models.CharField(
        max_length=7,
        choices=STATUS,
        default='open',
    )
    @admin.display(
        boolean=True,
        ordering="timestamp",
        description="Added recently?",
    )
    def was_added_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.title

