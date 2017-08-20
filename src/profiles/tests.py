import random
import string

import factory
from django.contrib.auth import get_user_model
from django.test import TestCase

from profiles.models import UserProfile, userStripe


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: "Agent %03d" % n)
    email = factory.LazyAttributeSequence(lambda o, n: f'{o.username}{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password')


class UserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory, password=random_string_generator())
    description = 'MyDescription'
    city = 'MyCity'
    website = 'MyWebsite'
    phone_number = 123456


class UserStripeFactory(factory.DjangoModelFactory):
    class Meta:
        model = userStripe

    user = factory.SubFactory(UserFactory, password=random_string_generator())
    stripe_id = 'MyStripeId'


class UserProfileTests(TestCase):
    def test_str(self):
        user_profile = UserProfileFactory()
        self.assertEqual(str(user_profile), user_profile.user.username)


class userStripeTests(TestCase):
    def test_str(self):
        user_stripe = UserStripeFactory()
        self.assertEqual(str(user_stripe), 'MyStripeId')
