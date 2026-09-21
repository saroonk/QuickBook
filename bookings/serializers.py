
from .models import Booking
from events.models import Event
from rest_framework.serializers import ModelSerializer,CharField,PrimaryKeyRelatedField
from rest_framework.exceptions import ValidationError



class BookingManageSerializer(ModelSerializer):
    user_username = CharField(source="user.username",read_only=True)
    event_name = CharField(source="event.name",read_only=True)
    class Meta:
        model = Booking
        fields = [
            "event","seats","status","created_at","user_username","event_name"
        ]
        extra_kwargs = {
            "event": {"write_only": True}
        }

    def validate(self, attrs):
        seat_count = attrs["seats"]

        if seat_count <= 0:
            raise ValidationError({
                "seats": "Seat count must be at least 1."
            })

        return attrs
