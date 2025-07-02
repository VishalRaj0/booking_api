from datetime import datetime
from django.db.models import Q
from rest_framework import serializers
from .models import Availability, Booking

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['id', 'user', 'day_of_week', 'start_time', 'end_time']

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("start_time must be before end_time")
        return data

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'date', 'start_time', 'end_time']

    def validate(self, data):
        user = data['user']
        date = data['date']
        start_time = data['start_time']
        end_time = data['end_time']

        delta = datetime.combine(date, end_time) - datetime.combine(date, start_time)
        minutes = delta.seconds // 60
        if minutes not in [15, 30, 45, 60]:
            raise serializers.ValidationError("Booking duration must be 15, 30, 45, or 60 minutes")

        overlapping = Booking.objects.filter(
            user=user,
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        if overlapping.exists():
            raise serializers.ValidationError("Booking overlaps with an existing booking")

        weekday = date.weekday()
        matches = Availability.objects.filter(
            user=user,
            day_of_week=weekday,
            start_time__lte=start_time,
            end_time__gte=end_time
        )
        if not matches.exists():
            raise serializers.ValidationError("Booking time is outside of user availability")

        return data
