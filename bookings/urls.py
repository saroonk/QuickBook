from django.urls import path
from .views import BookingManage,BookingCancel

urlpatterns = [
    path('bookings/',BookingManage.as_view(),name="bookingmanage"),
    path('bookings/<int:pk>/cancel/',BookingCancel.as_view(),name="bookingcancel")
]
