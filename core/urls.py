from django.contrib import admin
from django.urls import path
from genres.views import *
from actors.views import *
from movies.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name="genre-list-create"),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name="genre-retrieve-update-destroy"),

    path('actors/', ActorListCreateView.as_view(), name="actor-list-create"),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name="actor-retrieve-update-destroy"),
    
    path('movies/', MovieListCreateView.as_view(), name="movie-list-create"),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name="movie-retrieve-update-destroy"),
]
