from django.test import TestCase, Client
from .models import *
from .views import *
from django.urls import reverse,resolve
from django.contrib.auth.models import User

class TestModel(TestCase): #testing login
    def test_user(self):
        user = User.objects.create_user(username="username", password="password1", email="email@gmail.com", first_name="first_name", last_name="last_name")
        user.save()
        profile1 = UserProfile.objects.create(id=user.id,user = user,age=18,address="handigau")
        self.assertEqual(profile1.age,18)
        self.assertEqual(profile1.address,"handigau")

class TestURLS(TestCase):
    def test_list_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url).func,user_login)

# class testViews(testcase):
#     def test_views_weeb_GET(self):
#         client = Client()

#         response = clien.get(reverse('list'))

#         self.assertEquals(response.status_code,200)
#         self.asserTemplateUsed(response, 'login/list.html')