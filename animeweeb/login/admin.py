from django.contrib import admin
from .models import Anime,Rating,UserProfile
# Register your models here.
admin.site.register(Anime)
admin.site.register(UserProfile)
admin.site.register(Rating)
