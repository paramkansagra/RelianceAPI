from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import (
    OSName,
    HostName,
    OSVersion,
    BootDevice,
    Domain,
    LogonServer,
    OSBuildType,
    OSConfig,
    RegOwner,
    SystemBootTime,
    SystemModel,
    SystemType,
    WindowsDir,
)
from .serializers import (
    BootDeviceSerializer,
    DomainSerializer,
    OSBuildTypeSerializer,
    OSNameSerializer,
    HostNameSerializer,
    OSVersionSerializer,
    OSConfigSerializer,
    RegOwnerSerializer,
    SystemBootTimeSerializer,
    SystemModelSerializer,
    SystemTypeSerializer,
    WindowsDirSerializer,
    LogonServerSerializer,
)


class HostNameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HostName.objects.all()
    serializer_class = HostNameSerializer


class OSNameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OSName.objects.all()
    serializer_class = OSNameSerializer


class OSVersionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OSVersion.objects.all()
    serializer_class = OSVersionSerializer


class BootDeviceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BootDevice.objects.all()
    serializer_class = BootDeviceSerializer


class DomainViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class LogonServerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LogonServer.objects.all()
    serializer_class = LogonServerSerializer


class OSBuildTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OSBuildType.objects.all()
    serializer_class = OSBuildTypeSerializer


class OSConfigViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OSConfig.objects.all()
    serializer_class = OSConfigSerializer


class RegOwnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RegOwner.objects.all()
    serializer_class = RegOwnerSerializer


class SystemBootTimeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SystemBootTime.objects.all()
    serializer_class = SystemBootTimeSerializer


class SystemModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SystemModel.objects.all()
    serializer_class = SystemModelSerializer


class SystemTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SystemType.objects.all()
    serializer_class = SystemTypeSerializer


class WindowsDirViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WindowsDir.objects.all()
    serializer_class = WindowsDirSerializer
