from django.conf import settings
from django.db import models
from events.models import Event


class Booking(models.Model):

    status_choices = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    seats = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default='confirmed'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"



