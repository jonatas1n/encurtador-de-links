from django.test import TestCase, Client
from django.urls import reverse

from encurtador.models import Link
from encurtador.views import LinkForm

class TestNewLink(TestCase):

    def setUp(self):
        self.client     = Client()
        self.new_link   = reverse('encurtador:new_link')
        self.link = Link.objects

    def test_new_link_GET(self):
        response    = self.client.get(self.new_link)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encurtador/home.html')

    def test_new_link_POST(self):
        response = self.client.post(self.new_link, {
            'url'   : 'https://gitlab.com/pencillabs/encurtador-de-url' 
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.link.get(id=1).url, 'https://gitlab.com/pencillabs/encurtador-de-url')
