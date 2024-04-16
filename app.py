from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, World!")  # A simple view that returns a plain text response

urlpatterns = [
    path('', home, name='home'),  # Map the home view to the root URL
]

# Serving static files during development and in production if DEBUG is True
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serving media files in development and production if DEBUG is True
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
