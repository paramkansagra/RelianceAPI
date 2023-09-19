from django.urls import path, include
from .custom_push import dev

dev_data_view = dev.as_view({"post": "import_data"})

urlpatterns = [
    path("dev/" , dev_data_view , name = "dev"),
]