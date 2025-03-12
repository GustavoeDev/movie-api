from django.urls import path
from .views import *

urlpatterns = [
    path('actors/', ActorListCreateView.as_view(), name="actor-list-create"),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name="actor-retrieve-update-destroy"),
]