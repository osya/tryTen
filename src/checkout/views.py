import stripe
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY


class CheckoutView(LoginRequiredMixin, TemplateView):
    """
    CheckoutView based on TemplateView
    """
    template_name = 'checkout/checkout.html'

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context["publish_key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context

    def post(self, request, *args, **kwargs):
        token = request.POST.get('stripeToken')
        customer_id = request.user.userstripe.stripe_id
        customer = stripe.Customer.retrieve(customer_id)
        customer.sources.create(source=token)
        # Charge the user's card:
        charge = stripe.Charge.create(
                amount=1000,
                currency="eur",
                customer=customer,
                description="Example charge"
        )
        return self.get(request, *args, **kwargs)


# class CheckoutView(LoginRequiredMixin, FormView):
#     """
#     CheckoutView based on FormView
#     """
#     template_name = 'checkout/checkout.html'
#     form_class = CheckoutForm
#
#     def get_context_data(self, **kwargs):
#         context = super(CheckoutView, self).get_context_data(**kwargs)
#         context["publish_key"] = settings.STRIPE_PUBLISHABLE_KEY
#         return context
#
#     def form_valid(self, form):
#         token = form.cleaned_data['stripeToken']
#         customer_id = self.request.user.stripe_id
#         customer = stripe.Customer.retrieve(customer_id)
#         customer.sources.create(source=token)
#         # Charge the user's card:
#         charge = stripe.Charge.create(
#             amount=1000,
#             currency="eur",
#             customer=customer,
#             description="Example charge"
#         )
#         return super(CheckoutView, self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse('checkout')
