from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from pymongo import MongoClient
from django.conf import settings


def home(request):
    return render(request, 'main/home.html')

@login_required
def search(request):
    query = request.GET.get('q', '')
    results = []
    
    if query:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['jacuzzi_db']
        songs_collection = db['songs']
        
        # Search for songs matching the query
        results = list(songs_collection.find({
            '$or': [
                {'title': {'$regex': query, '$options': 'i'}},
                {'artist': {'$regex': query, '$options': 'i'}},
                {'album': {'$regex': query, '$options': 'i'}}
            ]
        }))
        
        client.close()
    
    return render(request, 'main/search_results.html', {
        'query': query,
        'results': results
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            # Authenticate user before login
            authenticated_user = authenticate(username=username, password=raw_password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('main:home')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})




