from django.contrib import admin
from . models import Moviedata,Directer,CensorInfo,Actor
# Register your models here.

admin.site.register(Moviedata)
admin.site.register(Directer)
admin.site.register(CensorInfo)
admin.site.register(Actor)