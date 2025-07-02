from rest_framework import viewsets, permissions
from .models import Availability, Booking
from .serializers import AvailabilitySerializer, BookingSerializer

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post']

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]  # public access
    http_method_names = ['get', 'post']         # only allow GET and POST
