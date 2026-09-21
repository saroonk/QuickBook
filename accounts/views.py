from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveAPIView
from .models import *
from rest_framework.views import APIView

from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination


class UserPagination(PageNumberPagination):
    page_size = 6

class UserManage(ListCreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    pagination_class = UserPagination


    def get_authenticators(self):
        if self.request and self.request.method == "POST":
            return []

        return [
            JWTAuthentication(),
            SessionAuthentication(),
        ]
    
    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]

        return [IsAdminUser()]

    def get_queryset(self):
        
        return User.objects.filter(is_staff=False)


class UserDetailView(RetrieveAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_queryset(self):   
        return User.objects.filter(is_staff=False)




class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {"detail": "Refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"detail": "Successfully logged out."},
                status=status.HTTP_200_OK
            )

        except Exception:
            return Response(
                {"detail": "Invalid or expired refresh token."},
                status=status.HTTP_400_BAD_REQUEST
            )



