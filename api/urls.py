from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

api_router = DefaultRouter()
api_router.register(r'bookings', views.BookingView, basename='booking')
api_router.register(r'menu', views.MenuView, basename='menu')

urlpatterns = [
    path('token-auth', obtain_auth_token, name='token-auth'),
    path('', include(api_router.urls)),
]