from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import WorkExperience, FeaturedProject, Contact
from django.core.mail import EmailMessage, get_connection
from django.conf import settings


def Menu(request):
    personal_projects = FeaturedProject.objects.all()
    work_experiences = WorkExperience.objects.all()

    context = {
        'personal_projects': personal_projects,
        'work_experiences': work_experiences,
    }
    return render(request, '.base/index.html', context)
