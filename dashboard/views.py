from accounts.models import User
from events.models import Vendor, Event
from bookings.models import Booking
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
class DashboardSummaryView(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [
        JWTAuthentication,
        SessionAuthentication,
    ]

    def get(self, request):
        return Response({
            "customers": User.objects.filter(is_staff=False).count(),
            "vendors": Vendor.objects.count(),
            "events": Event.objects.count(),
            "bookings": Booking.objects.count(),
        })





@staff_member_required
def dashboard_home(request):
    return render(request,"index.html")