from django.test import TestCase
from profiles.models import UserProfile, userStripe


# class UserProfileTests(TestCase):
#     def test_str(self):
#         u = UserProfile(name='MyName', description='MyDescription')
#         self.assertEqual(str(u), 'MyName')


class userStripeTests(TestCase):
    def test_str(self):
        u = userStripe(stripe_id='MyStripeId')
        self.assertEqual(str(u), 'MyStripeId')
