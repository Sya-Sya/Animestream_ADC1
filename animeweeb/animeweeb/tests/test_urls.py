from django.test import SimpleTestCase, Client 
#client, used to memic how the user can access our views

class TestUrls(SimpleTestCase):
    def test_login_url_is_resolved(self):
        assert 1 == 2

