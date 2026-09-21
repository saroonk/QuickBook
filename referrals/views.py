from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from .serializers import *
from .services import get_root_user, get_team_counts
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import PermissionDenied

class ReferralTreeView(APIView):
    authentication_classes = [SessionAuthentication,JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user != user and not request.user.is_staff:
            raise PermissionDenied(
                "You can only access your own referral root."
            )

        serializer = ReferralTreeSerializer(user)

        return Response(serializer.data)




class ReferralRootView(APIView):
    authentication_classes = [SessionAuthentication,JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)

        if request.user != user and not request.user.is_staff:
            raise PermissionDenied(
                "You can only access your own referral root."
            )

        root_user = get_root_user(user)

        serializer = ReferralRootSerializer(root_user)

        return Response(serializer.data)


class ReferralStatsView(APIView):
    authentication_classes = [SessionAuthentication,JWTAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user != user and not request.user.is_staff:
            raise PermissionDenied(
                "You can only access your own referral root."
            )

        stats = get_team_counts(user)

        return Response(stats)