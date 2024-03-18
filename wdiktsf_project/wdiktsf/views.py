from django.shortcuts import render
from django.http import JsonResponse
from .models import Artist, Song, Album

def artist_list(request):
    artists = Artist.objects.all().values('name')
    artist_list = list(artists)
    return JsonResponse(artist_list, safe=False)

def song_list(request):
    songs = Song.objects.all().values('title', 'artist')
    song_list = list(songs)
    return JsonResponse(song_list, safe=False)

def album_list(request):
    albums = Album.objects.all().values('title')
    album_list = list(albums)
    return JsonResponse(album_list, safe=False)