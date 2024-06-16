from rest_framework import viewsets
from .models import Hotel, Booking
from .serializers import HotelSerializer, BookingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['location', 'price_per_night']
    search_fields = ['name', 'description']


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def parse_sutochno(query):
    url = f"https://sutochno.ru/search?query={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for item in soup.select('.listing-item'):
        title = item.select_one('.title').text.strip()
        price = item.select_one('.price').text.strip()
        results.append({'title': title, 'price': price})

    return results


def search_view(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        results = parse_sutochno(query)
        return render(request, 'index.html', {'results': results})
    return render(request, 'index.html')
