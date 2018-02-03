import random
import string

import factory
from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase, TestCase
from django.urls import reverse


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: 'Agent %03d' % n)
    email = factory.LazyAttributeSequence(lambda o, n: f'{o.username}{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password')
    description = 'raw description'
    city = 'raw city'
    website = 'raw website'
    phone_number = 123456
    stripe_id = 'raw stripe_id'


class UserTests(TestCase):
    def test_create_user(self):
        UserFactory(password=random_string_generator())
        self.assertEqual(1, get_user_model().objects.count())


class IntegrationTests(LiveServerTestCase):
    def test_profile_home(self):
        response = self.client.get(reverse('profile'))
        self.assertIn(response.status_code, (301, 302))
