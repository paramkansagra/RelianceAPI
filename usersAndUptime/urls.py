from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import (
    HostNameViewSet,
    UptimeViewSet,
    UsersViewSet
)
from .custom_views import ImportDataViewSet

router = DefaultRouter()
router.register(r"host-name", HostNameViewSet)
router.register(r"up-time", UptimeViewSet)
router.register(r"users",UsersViewSet)

import_data_view = ImportDataViewSet.as_view({"post": "import_data"})

urlpatterns = [
    path("", include(router.urls)),
    path("import_data/", import_data_view, name="import-data"),
]
