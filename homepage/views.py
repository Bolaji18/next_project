from django.shortcuts import render
from django.http import HttpResponse
from .models import apartment

def home(request):
    all_images = apartment.objects.all()  # Get all instances of MyModel
    return render(request, 'index.html', {'images': all_images})

