from django.urls import path
from . import views


app_name = 'side'

urlpatterns = [
    path('search/', views.search_view, name='search'),
    path('artist/<str:artist_name>/', views.artist_profile, name='artist_profile'),
]
