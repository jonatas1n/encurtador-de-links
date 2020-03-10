from django.test import TestCase

from shortener.forms import LinkForm


class TestFormLink(TestCase):

    def setUp(self):
        self.form = LinkForm(data={'url' : 'https://gitlab.com/pencillabs'})

    def test_form_valid(self):
        self.assertTrue(self.form.is_valid())