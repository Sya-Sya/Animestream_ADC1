from django.test import TestCase,SimpleTestCase, Client
from .models import *
from .views import *
from django.urls import reverse,resolve

class Test_URL(SimpleTestCase): #testing urls
    def test_anime_list(self):
        url=reverse("login:anime")

        self.assertEquals(resolve(url).func,animelist)
