from django.shortcuts import render
from .models import Job

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def gallery(request):
    jobs    = Job.objects.all()
    context = {
        'jobs': jobs,
    }
    return render(request, 'pages/gallery.html', context)