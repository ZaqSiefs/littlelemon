from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu-item'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('api-token-auth', obtain_auth_token, name='api-token-auth'),
]