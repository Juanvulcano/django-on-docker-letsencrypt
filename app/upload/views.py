from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def image_upload(request):
    return render(request, "imstartup/index.html")


def typeform(request):
    return render(request, "darling.html")
