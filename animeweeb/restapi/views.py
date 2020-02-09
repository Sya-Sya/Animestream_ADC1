from django.shortcuts import render
from django.http import JsonResponse
import json
from login.models import Anime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def getAnime(request,page,size):
    if request.method == 'GET':
        skip = size * (page - 1)
        animes = Anime.objects.all()[skip:(page * size)]
        dict = {
            "animes": list(animes.values())
        }
        return JsonResponse(dict)
    else:
        return JsonResponse({"Status":"Error"})

@csrf_exempt
def deleteAnime(request,id):
    if request.method == 'DELETE' and Anime.objects.filter(id=id).exists():
        anime = Anime.objects.get(id=id)
        anime.delete()
        return JsonResponse({"Status":"Successfully deleted"})
    else:
        return JsonResponse({"Status":"Error"})

@csrf_exempt
def updateAnime(request,id):
    if request.method == 'PUT' and Anime.objects.filter(id=id).exists() and request.body:
        decoded_data = request.body.decode('utf-8')
        data = json.loads(decoded_data)
        anime = Anime.objects.get(id=id)
        anime.Anime_title = data['title']
        anime.Anime_description = data['description']
        anime.Anime_Category = data['category']
        anime.save()
        anime = Anime.objects.filter(pk=id)
        return JsonResponse({"anime":list(anime.values())})
    else:
        return JsonResponse({"Status":"Error","required":["title","description","category"]})

@csrf_exempt
def addAnime(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            des = request.POST.get('description')
            vid = request.FILES.get('video')
            cat = request.POST.get('category')
            userid = request.POST.get('userid')
            anime = Anime.objects.create(Anime_title =title , Anime_description=des, Anime_file=vid, Anime_Category=cat,user_id = userid)
            anime = Anime.objects.filter(id = anime.pk)
            #successful
            return JsonResponse({"anime":list(anime.values())})
        except Exception as ex:
            print(ex)
            return JsonResponse({"Status":"Internal server error"})
    else:
        return JsonResponse({"Status":"Error","required":["title","description","category","video","userid"]})
