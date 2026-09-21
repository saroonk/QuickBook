from django.urls import path

from .views import *

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('',UserManage.as_view(),name="user"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path('login/',TokenObtainPairView.as_view(),name="login"),
    path('refresh/',TokenRefreshView.as_view(),name="refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),

]
