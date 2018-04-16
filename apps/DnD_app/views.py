from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "DnD_app/index.html")

def register(request):
    return render(request, "DnD_app/profile.html")

def login(request):
    errors = User.objects.valid_login(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect ('/')
    else:
        request.session['user'] = User.objects.get(username=request.POST['username']).username
        request.session['id'] = User.objects.get(username=request.POST['username']).id
        return redirect ('/profile')

def new_Game(request):
    return render(request, "DnD_app/character.html")

def restart(request):
    return redirect ('/new_Game')

def keep_playing(request):
    return render(request, "DnD_app/game.html")

def game(request):
    return render(request, "DnD_app/game.html")
