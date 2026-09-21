from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *
from rest_framework.views import APIView

from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from .services import create_booking

from django.shortcuts import get_object_or_404

class BookingManage(ListCreateAPIView):
    serializer_class = BookingManageSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        else:
            return Booking.objects.filter(user=user)
        

    def perform_create(self, serializer):
        booking = create_booking(
            user=self.request.user,
            event_id=serializer.validated_data["event"].id,
            seats=serializer.validated_data["seats"],
        )

        serializer.instance = booking




class BookingCancel(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        instance = get_object_or_404(Booking,pk=pk,user=request.user)
        if instance.status == 'cancelled':
            raise ValidationError("This booking is already cancelled")
        instance.status = 'cancelled'
        instance.save()

        return Response(
            {"detail": "Booking cancelled successfully."},
            status=status.HTTP_200_OK
        )
