from rest_framework import viewsets
from .models import Hotel, Booking
from .serializers import HotelSerializer, BookingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['location', 'price_per_night']
    search_fields = ['name', 'description']


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


# bookings/views.py



