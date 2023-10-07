from django.shortcuts import render
from .models import WorkExperience,FeaturedProject

# Create your views here.

def Menu(request):
    personal_projects = FeaturedProject.objects.all()
    work_experiences = WorkExperience.objects.all()

    context = {
        'personal_projects': personal_projects,
        'work_experiences' : work_experiences,
    }

    return render(request, '.base/index.html', context)