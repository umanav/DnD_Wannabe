from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "DnD_app/index.html")

def register(request):
    return render(request, "DnD_app/profile.html")

def login(request):
    return render(request, "DnD_app/profile.html")

def new_Game(request):
    return render(request, "DnD_app/character.html")

def restart(request):
    return redirect ('/new_Game')

def keep_playing(request):
    return render(request, "DnD_app/game.html")

def game(request):
    return render(request, "DnD_app/game.html")
