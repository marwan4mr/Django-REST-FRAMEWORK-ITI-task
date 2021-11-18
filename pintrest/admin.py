from django.contrib import admin
from django.db.models import fields
from .models import Movie, Cast, Category, Seires

class MovieAdmin(admin.ModelAdmin):
    class meta:
        model = Movie
        fields = '__all__'


# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Cast)
admin.site.register(Category)
admin.site.register(Seires)
