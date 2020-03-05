from django.test import TestCase

from encurtador.models import Link


class TestLink(TestCase):

    def setUp(self):
        self.link = Link.objects.create(
            url     = 'https://gitlab.com/pencillabs'
        )

    def test_url(self):        
        self.assertEqual(
            str(self.link),
            ('https://gitlab.com/pencillabs')
        )