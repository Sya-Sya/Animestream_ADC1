from django.test import TestCase,SimpleTestCase, Client
from .models import *
from .views import *
from .urls import *
from django.urls import reverse,resolve
from django.contrib.auth.models import User

class Test_URL(TestCase): #testing urls
    def test_user(self):
        user = User.objects.create_user(username="username", password="password1", email="email@gmail.com", first_name="first_name", last_name="last_name")
        user.save()
        profile1 = UserProfile.objects.create(id=user.id,user = user,age=18,address="handigau")
        self.assertEqual(profile1.age,18)
        self.assertEqual(profile1.address,"handigau")

# class Test_view(SimpleTestCase):   #testing views
#     def test_register(self):
#         c=Client()
#         url=reverse("login:register") #reverse is used to show path 
#         response=c.get(url)
#         self.assertEquals(response.status_code,200)
    
#     def test_login(self):   # testing login
#         c=Client()
#         url=reverse("login:login")
#         response=c.get(url)
#         self.assertEquals(response.status_code,200)

# class Test(TestCase): #Model testing     
    # def test_dESC(self):
    #     desc = Anime.objects.create(user="Animeislifenibb", address="nekoneko@gmail.com",
    #                                   age = "50"
    #                                   )
    #     use = Anime.objects.get(user="Animeislifenibb")
    #     self.assertEquals(use.user,"Animeislifenibb")
    
    # def test_title(self):
    #     desc = Anime.objects.create(user="prashantiaunt", address="nekoneko@gmail.com",
    #                                  age = "50"
    #                                   )
    #     self.assertTrue(desc.TestTitle())