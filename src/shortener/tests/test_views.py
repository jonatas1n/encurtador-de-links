from django.test import TestCase, Client
from django.urls import reverse

from shortener.models import Link
from shortener.views import LinkForm

class TestNewLink(TestCase):

    def setUp(self):
        self.client         = Client()
        self.new_link       = reverse('shortener:new_link')
        self.link           = Link.objects

    def test_new_link_GET(self):
        response    = self.client.get(self.new_link)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shortener/home.html')

    def test_new_link_POST(self):
        response    = self.client.post(self.new_link, {
            'url'   : 'https://gitlab.com/pencillabs/encurtador-de-url' 
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.link.get(id=1).url, 'https://gitlab.com/pencillabs/encurtador-de-url')

class TestGetShortener(TestCase):
    
    def setUp(self):
        self.client         = Client()
        self.new_link       = reverse('shortener:new_link')
        self.client.post(self.new_link, {'url' : 'https://gitlab.com/pencillabs/encurtador-de-url'})

    def test_get_shortener_GET(self):
        self.get_shortener  = (reverse('shortener:get_shortener', args=['867nv']))
        response            = self.client.get(self.get_shortener)

        self.assertEqual(response.status_code, 302)

    def test_get_shortener_get(self):
        self.get_shortener  = (reverse('shortener:get_shortener', args=['867n3']))
        response            = self.client.get(self.get_shortener)

        self.assertEqual(response.status_code, 404)

class TestGetUrlRank(TestCase):

    def setUp(self):
        self.client         = Client()
        self.get_url_rank   = reverse('shortener:get_url_rank')

    def test_rank_url_GET(self):
        response    = self.client.get(self.get_url_rank)

        self.assertEqual(response.status_code, 200)

