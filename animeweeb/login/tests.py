from django.test import TestCase,SimpleTestCase, Client
from login.models import *
from login.views import *
from django.urls import reverse,resolve

class Test_URL(SimpleTestCase): #testing urls
    def test_anime_list(self):
        url=reverse("login:anime")

        self.assertEquals(resolve(url).func,animelist)

class Test_view(SimpleTestCase):   #testing views
    def test_register(self):
        c=Client()
        url=reverse("login:register") #reverse is used to show path 
        response=c.get(url)
        self.assertEquals(response.status_code,200)
    
    def test_login(self):   # testing login
        c=Client()
        url=reverse("login:login")
        response=c.get(url)
        self.assertEquals(response.status_code,200)

class Test(TestCase): #Model testing     
    def test_dESC(self):
        desc = Anime.objects.create(user="Animeislifenibb", address="nekoneko@gmail.com",
                                      age = "50"
                                      )
        use = Anime.objects.get(user="Animeislifenibb")
        self.assertEquals(use.user,"Animeislifenibb")
    
    def test_title(self):
        desc = Anime.objects.create(user="prashantiaunt", address="nekoneko@gmail.com",
                                     age = "50"
                                      )
        self.assertTrue(desc.TestTitle())