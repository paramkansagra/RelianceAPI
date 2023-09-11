from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import HostName,Users,Uptime
from .serializers import HostNameSerializer,UsersSerializer,UptimeSerializer

class HostNameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HostName.objects.all()
    serializer_class = HostNameSerializer

class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UptimeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Uptime.objects.all()
    serializer_class = UptimeSerializer