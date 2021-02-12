import os
import api
import unittest
import tempfile

class Test_unit(unittest.TestCase):
    def setUp(self):
        self.app = api.app.test_client()
        self.app.get('/create')

    def test_evaluate_db(self):
        # Tests the none request in API
        res = self.app.get('/')
        assert b'success' in res.data

    ## /add
    def test_add_valid_url(self):
        # Tests valid URL insertion to DB
        # Expected Result: Success
        res = self.app.get('/add?url=%s&short=' % 'https://www.devmedia.com.br/boas-praticas-em-tdd/40167')
        assert b'success' in res.data

    def test_add_repeated_url(self):
        # Tests repeated URL insertion to DB
        # Expected result: Error
        res = self.app.get('/add?url=%s&short=' % 'https://realpython.com/python-string-formatting/#1-old-style-string-formatting-operator')
        assert b'error' in res.data
    
    def test_add_invalid_url(self):
        # Tests invalid URL insertion to DB
        # Expected Result: Error
        res = self.app.get('/add?url=%s&short=' % 'australopithecus')
        assert b'error' in res.data

    def test_add_prohibited_url(self):
        # Tests prohibited URL insertion to DB
        # Expected Result: Error
        res = self.app.get('/add?url=%s&short=' % 'petit.com')
        assert b'error' in res.data

    ## /redirect
    def test_redirect_valid_link(self):
        # Tests the redirection of a existent link redirecting on DB
        # Expected Result: Success
        res = self.app.get('/redirect?link=%s' % 'XhYdtz')
        assert b'success' in res.data

    def test_redirect_invalid_link(self):
        # Tests the redirection of a non-existent link redirecting on DB
        # Expected Result: Error
        res = self.app.get('/redirect?link=%s' % 'abcdef')
        assert b'error' in res.data

    ## /rank
    def test_rank(self):
        # Tests request of 5 most accessed link on Petit page
        res = self.app.get('/rank')
        assert b'success' in res.data


if __name__ == '__main__':
    unittest.main()