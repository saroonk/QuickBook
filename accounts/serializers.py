from .models import User
from rest_framework.serializers import ModelSerializer,CharField,PrimaryKeyRelatedField
from rest_framework.exceptions import ValidationError
from referrals.services import find_placement

class RegisterSerializer(ModelSerializer):

    refer_code = CharField(write_only=True,allow_blank=True,required=False)
    referral_code =  CharField(read_only=True)
    class Meta:
        model = User
        fields = [ "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "refer_code",
            "referral_code"
            ]
        extra_kwargs = {
            "password": {"write_only": True}
        }
    
    def validate(self, attrs):
        refer_code = attrs.get("refer_code")

        if refer_code:
            referred_user = User.objects.filter(
                referral_code=refer_code
            ).first()

            if not referred_user:
                raise ValidationError({
                    "refer_code": "Invalid referral code."
                })

        return attrs

    def create(self, validated_data):
        refer_code = validated_data.pop("refer_code", None)

        referred_user = None
        parent = None
        position = None

        if refer_code:
            referred_user = User.objects.get(
                referral_code=refer_code
            )

            parent, position = find_placement(referred_user)

        return User.objects.create_user(
            referred_by=parent,
            position=position,
            **validated_data
        )




