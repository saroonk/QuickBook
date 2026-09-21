from django.db import models

# Create your models here.
from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name="events"
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    total_seats = models.PositiveIntegerField()

    def __str__(self):
        return self.name