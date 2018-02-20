from django.test import LiveServerTestCase
from django.urls import reverse


class IntegrationTests(LiveServerTestCase):
    def test_checkout_home(self):
        response = self.client.get(reverse('checkout'))
        self.assertIn(response.status_code, (301, 302))
