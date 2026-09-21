from django.urls import path

from .views import *


urlpatterns = [
    path('events/',EventMange.as_view(),name="eventmanage"),
    path('events/<int:pk>/',EventDetailView.as_view(),name="eventdetail"),
    path('vendors/',VendorMange.as_view(),name="vendormanage"),
    path('vendors/<int:pk>/',VendorDetailView.as_view(),name="vendordetail"),

]
