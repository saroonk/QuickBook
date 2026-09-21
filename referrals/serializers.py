from rest_framework import serializers
from accounts.models import User


class ReferralTreeSerializer(serializers.ModelSerializer):
    left = serializers.SerializerMethodField()
    right = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "referral_code",
            "left",
            "right",
        ]

    def get_left(self, obj):
        user = obj.referrals.filter(position="left").first()

        if not user:
            return None

        return ReferralTreeSerializer(user).data

    def get_right(self, obj):
        user = obj.referrals.filter(position="right").first()

        if not user:
            return None

        return ReferralTreeSerializer(user).data



class ReferralRootSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "referral_code",
        ]


class ReferralStatsSerializer(serializers.Serializer):
    left_count = serializers.IntegerField()
    right_count = serializers.IntegerField()