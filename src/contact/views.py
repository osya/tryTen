from braces.views import FormValidMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from contact.forms import ContactForm


class ContactView(FormValidMessageMixin, FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    form_valid_message = 'Thanks for the message. We will get right back to you'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        response = super(ContactView, self).form_valid(form)
        # subject = 'Message from MYSITE.com'
        # message = f'{form.cleaned_data["name"]} {form.cleaned_data["comment"]}'
        # email_from = form.cleaned_data['email']
        # email_to = [settings.EMAIL_HOST_USER]
        # send_mail(subject, message, email_from, email_to, fail_silently=False)
        return response
