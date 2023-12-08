from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from restaurant.models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

class MenuView(viewsets.ModelViewSet):
    model = Menu
    queryset = model.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class BookingView(viewsets.ModelViewSet):
    model = Booking
    queryset = model.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]