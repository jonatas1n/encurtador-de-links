from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Sum

from shortener.models import Link
from shortener.views import LinkForm, create_content, create_context

class TestUnitaryView(TestCase):

    def setUp(self):
        self.client         = Client()
        self.link           = Link.objects
        self.new_link       = reverse('shortener:new_link')
        self.client.post(self.new_link, {'url' : 'https://gitlab.com/pencillabs/encurtador-de-url'})

    def test_create_content(self):
        self.content        = create_content()

        content = {'link': 'https://gitlab.com/pencillabs/...', 'short_url': '0.0.0.0:8000/867nv', 'short_code': '867nv'}
        self.assertEqual(self.content, content)

    def test_create_context(self):
        self.context        = create_context()
        print(self.context['urls'][0])

        context = {'url': 'https://gitlab.com/pencillabs/encurtador-de-url', 'access__sum': 0}
        self.assertEqual(self.context['urls'][0], context)