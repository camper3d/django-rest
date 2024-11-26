from . models import Phone
from .serializers import PhoneSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from . permissions import ALLForAdminOtherReadOnly
import django_filters
from rest_framework import filters

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = (ALLForAdminOtherReadOnly, )
    filter_backends = [filters.OrderingFilter]
    search_fields = ['brand', 'display', 'battery', 'price_blr']
