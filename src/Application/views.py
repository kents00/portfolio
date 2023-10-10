from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import WorkExperience,FeaturedProject, Contact
from django.core.mail import EmailMessage, get_connection
from django.conf import settings

def Menu(request):
    personal_projects = FeaturedProject.objects.all()
    work_experiences = WorkExperience.objects.all()

    context = {
        'personal_projects': personal_projects,
        'work_experiences' : work_experiences,
    }
    return render(request, '.base/index.html', context)

def send_mail(request):
    if request.method == "POST":
       with get_connection(
           host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS
       ) as connection:
           subject = 'New Contact Submission'
           email_from = settings.EMAIL_HOST_USER
           recipient_list = [request.POST.get("email")]
           message = f'You have a new contact submission from: {request.POST.get("email")}'
           EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
           return HttpResponseRedirect('')
    else:
           return render(request, '.base/index.html')
