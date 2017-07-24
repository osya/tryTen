from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from braces import views
from .forms import ContactForm


class ContactView(views.FormValidMessageMixin, generic.FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    form_valid_message = 'Thanks for the message. We will get right back to you'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        response = super(ContactView, self).form_valid(form)
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE.com'
        message = '%s %s' % (comment, name)
        email_from = form.cleaned_data['email']
        email_to = [settings.EMAIL_HOST_USER]
        # send_mail(subject, message, email_from, email_to, fail_silently=False)
        return response
