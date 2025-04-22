from django.urls import path
from django.contrib.auth.views import LogoutView    
from . import views


app_name = 'main'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='main:home'), name='logout'),
]

