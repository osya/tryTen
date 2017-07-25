import stripe
from django.conf import settings
from django.views import generic
from braces import views

stripe.api_key = settings.STRIPE_SECRET_KEY


class CheckoutView(views.LoginRequiredMixin, generic.TemplateView):
    template_name = 'checkout/checkout.html'

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

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context["publish_key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context
