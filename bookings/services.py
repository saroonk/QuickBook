from django.db import transaction
from django.db.models import Sum

from .models import Booking
from events.models import Event
from rest_framework.exceptions import ValidationError
def get_available_seats(event):
    booked_seats = Booking.objects.filter(
        event=event,
        status='confirmed'
    ).aggregate(
        total=Sum("seats")
    )["total"] or 0

    return event.total_seats - booked_seats


@transaction.atomic
def create_booking(user, event_id, seats):
    try:
        event = Event.objects.select_for_update().get(id=event_id)
    except Event.DoesNotExist:
        raise ValidationError({
            "event": "Event not found."
        })

    available_seats = get_available_seats(event)

    if seats > available_seats:
        raise ValidationError("Not enough seats available")

    booking = Booking.objects.create(
        user=user,
        event=event,
        seats=seats,
        status='confirmed'
    )

    return booking