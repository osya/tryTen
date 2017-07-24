from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views import generic
from braces import views
from .forms import contactForm


def contact(request):
    headline = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE.com'
        message = '%s %s' % (comment, name)
        email_from = form.cleaned_data['email']
        email_to = [settings.EMAIL_HOST_USER]
        # send_mail(subject, message, email_from, email_to, fail_silently=False)
        headline = 'Thanks'
        confirm_message = 'Thanks for the message. We will get right back to you'
        form = None
    context = {'headline': headline, 'form': form, 'confirm_message': confirm_message}
    return render(request, 'contact/contact.html', context)


# class ContactView(views.SetHeadlineMixin, generic.TemplateView):
#     template_name = 'contact/contact.html'
#     headline = 'Contact'
