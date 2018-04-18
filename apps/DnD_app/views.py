from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index(request):
    if 'id' not in request.session:
        return render(request, "DnD_app/index.html")
    return redirect("/profile")

def register(request):
    result = User.objects.valid_registration(request.POST)
    if result[1] == False:
        request.session['id'] = result[0].id
        request.session['user_name'] = result[0].username
        return redirect("/profile")
    else:
        for error in result[0]: 
            messages.error(request, error)
    return redirect("/")

def profile(request):
    user=User.objects.get(id=request.session['id'])
    return render(request,'DnD_app/profile.html')

def login(request):
    errors = User.objects.valid_login(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect ('/')
    else:
        request.session['user_name'] = User.objects.get(username=request.POST['username']).username
        request.session['id'] = User.objects.get(username=request.POST['username']).id
        return redirect ('/profile')

def logout(request):
    del request.session['id']
    return redirect('/')

def new_Game(request):
    characters = Character.objects.all()
    return render(request, "DnD_app/character.html",{'characters':characters})

def save(request):
    active = Game.objects.active_game(request.session['id'])
    if active[0] == False:
        user= User.objects.get(id=request.session['id'])
        game= Game.objects.create(user = user, hp = request.session['hp'], gold=request.session['gold'], level=request.session['level'])
    else:
        for active_game in active[1]: 
            game = Game.objects.get(id=active_game.id)
            game.hp = request.session['hp']
            game.gold = request.session['gold']
            game.level = request.session['level']
    return redirect('/profile')

def restart(request):
    del request.session['gold']
    del request.session['hp']
    del request.session['level']
    current = Game.objects.get(user_id=request.session['id'])
    current.delete()
    return redirect ('/new_Game')

def keep_playing(request):
    return render(request, "DnD_app/game.html")

def game(request, id):
    character = Character.objects.get(id=id)
    request.session['hp'] = character.hp
    request.session['gold'] = character.gold
    request.session['level'] = 1
    return render(request, "DnD_app/game.html")
