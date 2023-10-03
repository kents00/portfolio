from django.shortcuts import render
from django.http import request
from .models import WorkExperience,FeaturedProject

# Create your views here.

def Menu(request):
    projects = WorkExperience.objects.all()
    work_experience = FeaturedProject.objects.all()

    context = {
        'projects':projects,
        'work_experience' : work_experience,
    }

    return render(request, '.base/index.html', context)