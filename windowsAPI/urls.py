from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import (
    OSNameViewSet,
    HostNameViewSet,
    OSVersionViewSet,
    OSBuildTypeViewSet,
    BootDeviceViewSet,
    DomainViewSet,
    LogonServerViewSet,
    OSConfigViewSet,
    RegOwnerViewSet,
    SystemBootTimeViewSet,
    SystemModelViewSet,
    WindowsDirViewSet,
    SystemTypeViewSet,
)
from .custom_views import ImportDataViewSet

router = DefaultRouter()
router.register(r"os-name", OSNameViewSet)
router.register(r"os-version", OSVersionViewSet)
router.register(r"os-config", OSConfigViewSet)
router.register(r"os-build-type", OSBuildTypeViewSet)
router.register(r"host-name", HostNameViewSet)
router.register(r"boot-device", BootDeviceViewSet)
router.register(r"domain", DomainViewSet)
router.register(r"logon", LogonServerViewSet)
router.register(r"reg-owner", RegOwnerViewSet)
router.register(r"system-boot", SystemBootTimeViewSet)
router.register(r"os-model", SystemModelViewSet)
router.register(r"windows-dir", WindowsDirViewSet)
router.register(r"system-type", SystemTypeViewSet)

import_data_view = ImportDataViewSet.as_view({"post": "import_data"})

urlpatterns = [
    path("", include(router.urls)),
    path("import_data/", import_data_view, name="import-data"),
]
