from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import WorkExperience,FeaturedProject, Contact
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy

def Menu(request):
    personal_projects = FeaturedProject.objects.all()
    work_experiences = WorkExperience.objects.all()

    context = {
        'personal_projects': personal_projects,
        'work_experiences' : work_experiences,
    }
    return render(request, '.base/index.html', context)

class ContactView(FormView):
    template_name = '.base/index.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

