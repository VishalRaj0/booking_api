from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AvailabilityViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'availability', AvailabilityViewSet, basename='availability')
router.register(r'booking', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]
