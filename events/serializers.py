
from .models import Event,Vendor
from rest_framework.serializers import ModelSerializer,CharField,PrimaryKeyRelatedField
from rest_framework.exceptions import ValidationError




class EventManageSerializer(ModelSerializer):
    vendor_name = CharField(source="vendor.name",read_only=True)
    class Meta:
        model = Event
        fields = [
            "id","vendor","name","description","event_date","total_seats","vendor_name"

        ]
        # extra_kwargs = {
        #     "vendor": {"write_only": True}
        # }



class VendorManageSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "id","name","email","phone","address"
        ]
    def validate_email(self, value):
        if Vendor.objects.filter(email=value).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise ValidationError("A vendor with this email already exists.")
        return value
    def validate_phone(self, value):
        if Vendor.objects.filter(phone=value).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise ValidationError("A vendor with this phone number already exists.")
        return value