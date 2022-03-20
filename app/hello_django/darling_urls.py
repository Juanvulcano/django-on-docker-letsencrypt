from django.contrib import admin
from django.urls import path
from django.conf import settings
from upload.views import image_upload, typeform


urlpatterns = [
    path("", typeform, name=""),
]
