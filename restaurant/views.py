from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import UserSerializer, BookingSerializer, MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserView(viewsets.ModelViewSet):
    model = User
    queryset = model.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class MenuItemView(ListCreateAPIView):
    model = Menu
    queryset = model.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    model = Menu
    queryset = model.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class BookingView(ListCreateAPIView):
    model = Booking
    queryset = model.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class SingleBookingView(RetrieveUpdateDestroyAPIView):
    model = Booking
    queryset = model.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
