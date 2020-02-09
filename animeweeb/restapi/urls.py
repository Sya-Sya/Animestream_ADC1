from django.urls import path
from . import views

urlpatterns = [
    path('page/<int:page>/size/<int:size>/',views.getAnime,name="getAnime"),
    path('add/',views.addAnime,name="addAnime"),
    path('delete/<int:id>/',views.deleteAnime,name="deleteAnime"),
    path('update/<int:id>/',views.updateAnime,name="updateAnime"),
]