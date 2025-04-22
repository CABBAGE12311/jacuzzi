from django.shortcuts import render
from pymongo import MongoClient
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils.html import escape
from django.http import JsonResponse
import re
from .models import Artist
from .models import Song



@login_required
def artist_profile(request, artist_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['jacuzzi_db']
    artists_collection = db['artists']
    songs_collection = db['songs']

    # Get artist data
    artist = artists_collection.find_one({'name': artist_name})
    if artist:
        artist['_id'] = str(artist['_id'])  # For safety
        songs = list(songs_collection.find({'artist': artist_name}))
        for song in songs:
            song['_id'] = str(song['_id'])
    else:
        artist = {'name': artist_name, 'image_url': None}
        songs = []

    return render(request, 'main/artist_profile.html', {
        'artist': artist,
        'songs': songs
    })

def search_view(request):
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    results = []

    if query:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['jacuzzi_db']
        collection = db['songs']

        mongo_results = list(collection.find({
            "$or": [
                {"title": {"$regex": re.escape(query), "$options": "i"}},
                {"artist": {"$regex": re.escape(query), "$options": "i"}},
                {"album": {"$regex": re.escape(query), "$options": "i"}}
            ]
        }))

        for result in mongo_results:
            result['_id'] = str(result['_id'])
            result.setdefault('album', '')
            results.append(result)

        paginator = Paginator(results, 10)
        try:
            results = paginator.page(page)
        except:
            results = paginator.page(1)

    if is_ajax:
        return JsonResponse({
            'results': list(results) if isinstance(results, Paginator) else results,
            'query': query
        })

    return render(request, 'main/search_results.html', {
        'results': results,
        'query': query
    })
