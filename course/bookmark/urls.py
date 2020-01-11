from django.urls import path
from bookmark import views

urlpatterns = [
    path('bookmark', views.bookmark, name='bookmark'),
    path('home',views.home, name='home'),
    path('login',views.login, name='login')
]
