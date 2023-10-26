from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    inquiry = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

    def get_formatted_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        cleaned_data = super().clean()

        name = cleaned_data.get('name').strip()
        from_email = cleaned_data.get('email')
        subject = cleaned_data.get('inquiry')

        msg = f'{name} with email {from_email} said:\n"{subject}"\n\n'
        msg += cleaned_data.get('message')

        return subject, msg

    def send_email(self):
        subject, msg = self.get_formatted_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )
