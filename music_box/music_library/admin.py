from django.contrib import admin

from .models import  Artist, Album, Track, Language, Company, Lyric, Genre

admin.site.register(Company)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Language)
admin.site.register(Lyric)

