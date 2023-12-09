from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = "api"
menu_router = DefaultRouter()
bookings_router = DefaultRouter()

menu_router.register(r'menu', views.MenuView)
bookings_router.register(r'bookings', views.BookingView)


urlpatterns = [
    path('token-auth', obtain_auth_token, name='token-auth'),
    path('', include(menu_router.urls)),
    path('', include(bookings_router.urls)),
]