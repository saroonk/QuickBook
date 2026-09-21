from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *
from rest_framework.views import APIView

from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsStaffOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .filters import EventFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import ScopedRateThrottle
class EventMange(ListCreateAPIView):
    serializer_class = EventManageSerializer
    queryset = Event.objects.all()
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = EventFilter
    search_fields = ["name"]
    ordering_fields = ["event_date", "total_seats"]
    authentication_classes = [
        JWTAuthentication,
        SessionAuthentication,
    ]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "events"

class EventDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventManageSerializer
    queryset = Event.objects.all()
    permission_classes = [IsStaffOrReadOnly]
    authentication_classes = [
        JWTAuthentication,
        SessionAuthentication,
    ]
    


class VendorMange(ListCreateAPIView):
    serializer_class = VendorManageSerializer
    queryset = Vendor.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [
        JWTAuthentication,
        SessionAuthentication,
    ]

class VendorDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = VendorManageSerializer
    queryset = Vendor.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [
        JWTAuthentication,
        SessionAuthentication,
    ]
