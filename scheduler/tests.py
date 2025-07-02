from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Availability, Booking

User = get_user_model()

class BookingAPITests(APITestCase):
    def setUp(self):

        self.user = User.objects.create(username='testuser')
        Availability.objects.create(user=self.user, day_of_week=0, start_time="09:00", end_time="10:00")

    def test_create_valid_booking(self):
        url = reverse('booking-list')
        data = {
            'user': self.user.id,
            'date': '2025-01-06',
            'start_time': '09:00',
            'end_time': '09:15'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

    def test_booking_invalid_duration(self):
        url = reverse('booking-list')
        data = {
            'user': self.user.id,
            'date': '2025-01-06',
            'start_time': '09:00',
            'end_time': '09:20'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('duration', str(response.data).lower())

    def test_booking_outside_availability(self):
        url = reverse('booking-list')
        data = {
            'user': self.user.id,
            'date': '2025-01-06',
            'start_time': '08:45',
            'end_time': '09:00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_overlapping_bookings(self):
        Booking.objects.create(user=self.user, date='2025-01-06', start_time="09:00", end_time="09:15")
        url = reverse('booking-list')
        data = {
            'user': self.user.id,
            'date': '2025-01-06',
            'start_time': '09:10',
            'end_time': '09:25'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class AvailabilityAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')

    def test_create_availability(self):
        url = reverse('availability-list')
        data = {
            'user': self.user.id,
            'day_of_week': 2,
            'start_time': '14:00',
            'end_time': '15:00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Availability.objects.count(), 1)

    def test_invalid_availability(self):
        url = reverse('availability-list')
        data = {
            'user': self.user.id,
            'day_of_week': 2,
            'start_time': '15:00',
            'end_time': '14:00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
