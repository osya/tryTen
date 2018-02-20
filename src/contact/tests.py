# Create your tests here.
from django.test import LiveServerTestCase
from django.urls import reverse


class IntegrationTests(LiveServerTestCase):
    def test_contact_home(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
