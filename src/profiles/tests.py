import random
import string

import factory
from django.contrib.auth import get_user_model
from django.test import TestCase


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: 'Agent %03d' % n)
    email = factory.LazyAttributeSequence(lambda o, n: f'{o.username}{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password')
    description = 'MyDescription'
    city = 'MyCity'
    website = 'MyWebsite'
    phone_number = 123456
    stripe_id = 'MyStripeId'


class UserTests(TestCase):
    def test_str(self):
        user = UserFactory(password=random_string_generator())
        self.assertEqual(str(user), user.username)
