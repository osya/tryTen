import random
import string

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase, RequestFactory, TestCase
from django.urls import reverse

import chromedriver_binary
import factory
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

from categories.tests import CategoryFactory
from goods.models import Good
from goods.views import GoodList


def random_string_generator(size=10,
                            chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# pragma pylint: disable=R0903
class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: 'Agent %03d' % n)
    email = factory.LazyAttributeSequence(
        lambda o, n: f'{o.username}{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password')


class GoodFactory(factory.DjangoModelFactory):
    class Meta:
        model = Good

    name = 'raw good name'
    description = 'raw good description'
    category = factory.SubFactory(CategoryFactory)
    in_stock = True
    price = 100.0


# pragma pylint: enable=R0903


class GoodTests(TestCase):
    def test_str(self):
        good = GoodFactory()
        self.assertEqual(1, Good.objects.count())
        self.assertEqual('raw good name', good.name)


class GoodListViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserFactory(password=random_string_generator())

    def test_no_goods_in_context(self):
        request = self.factory.get('/')
        request.user = self.user
        response = GoodList.as_view()(request)
        self.assertEqual(
            list(response.context_data['object_list']),
            [],
        )

    def test_goods_in_context(self):
        request = self.factory.get('/')
        good = GoodFactory()
        request.user = self.user
        response = GoodList.as_view()(request)
        self.assertEqual(
            list(response.context_data['object_list']),
            [good],
        )


class CreatePostIntegrationTest(LiveServerTestCase):
    selenium = None

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        # Following two lines needed to fix "selenium.common.exceptions.WebDriverException: Message: unknown error:
        # Chrome failed to start: crashed" in Travis CI
        chrome_options.add_argument('--window-size=1024,768')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--log-level=3')
        cls.selenium = webdriver.WebDriver(
            executable_path=chromedriver_binary.chromedriver_filename,
            chrome_options=chrome_options)
        cls.password = random_string_generator()
        super(CreatePostIntegrationTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(CreatePostIntegrationTest, cls).tearDownClass()

    def setUp(self):
        # `user` creation placed in setUp() rather than setUpClass(). Because when `user` created in setUpClass then
        # `test_good_create` passed when executed separately, but failed when executed in batch
        # TODO: investigate this magic
        self.user = UserFactory(password=self.password)

    def test_good_list(self):
        response = self.client.get(reverse('goods:list'))
        self.assertEqual(response.status_code, 200)

    def test_slash(self):
        response = self.client.get(reverse('home'))
        self.assertIn(response.status_code, (301, 302))

    def test_empty_create(self):
        response = self.client.get(reverse('goods:create'))
        self.assertIn(response.status_code, (301, 302))

    def test_good_create(self):
        self.assertTrue(
            self.client.login(
                username=self.user.username, password=self.password))
        cookie = self.client.cookies[settings.SESSION_COOKIE_NAME]
        # Replace `localhost` to 127.0.0.1 due to the WinError 10054 according to the
        # https://stackoverflow.com/a/14491845/1360307
        self.selenium.get(
            f'{self.live_server_url}{reverse("goods:create")}'.replace(
                'localhost', '127.0.0.1'))
        if cookie:
            self.selenium.add_cookie({
                'name': settings.SESSION_COOKIE_NAME,
                'value': cookie.value,
                'secure': False,
                'path': '/'
            })
        CategoryFactory()
        self.selenium.refresh()  # need to update page for logged in user
        self.selenium.find_element_by_id('id_name').send_keys('raw good name')
        self.selenium.find_element_by_id('id_description').send_keys(
            'raw category description')
        select = Select(self.selenium.find_element_by_id('id_category'))
        all_options = [o.get_attribute('value') for o in select.options]
        select.select_by_value(all_options[1])
        self.selenium.find_element_by_id('id_price').send_keys('100.0')
        self.selenium.find_element_by_xpath(
            '//*[@id="submit-id-submit"]').click()
        self.assertEqual(1, Good.objects.count())
        self.assertEqual('raw good name', Good.objects.first().name)
