from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from login.models import Anime
# Create your views here.
@login_required(login_url="/login/")
def members(request):
    animes = Anime.objects.filter(user_id = request.user.id)
    if request.method == "POST":
        title = request.POST.get('title')
        des = request.POST.get('des')
        vid = request.FILES.get('vid')
        cat = request.POST.get('cat')
        try:
            Anime.objects.create(Anime_title =title , Anime_description=des, Anime_file=vid, Anime_Category=cat,user_id = request.user.id)
        except Exception as ex:
            print(ex)
            return HttpResponse('Internal server error')
        #successful
        return redirect('anime')

    else:
        return render(request, "members/profile.html", context={"animes":animes})