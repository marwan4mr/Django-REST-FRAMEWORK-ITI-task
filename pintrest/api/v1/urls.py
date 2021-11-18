from django.urls import path
from . import views
from django.conf import settings
urlpatterns=[

    path('movies/', views.movie_index),
    path('movies/<int:movie_id>', views.handle_movie)
]


