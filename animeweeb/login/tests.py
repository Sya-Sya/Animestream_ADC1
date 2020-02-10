from django.test import TestCase,SimpleTestCase, Client
from .models import *
from .views import *
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
        desc = Anime.objects.create(Anime_title="Animeislifenibb", upload_date="2002-06-02",
                                      movie_description = "hi there whats up jhcv dcb d b ."
                                      )
        use=Anime.objects.get(Anime_title="chartpaper")
        self.assertEquals(use.movie_title,"chartpaper")
    
    def test_title(self):
        desc = Movies.objects.create(movie_title="Lotlot", release_date="2002-06-02",
                                      movie_description = "hi there whats up jhcv dcb d b ."
                                      )
        self.assertTrue(desc.TestTitle())