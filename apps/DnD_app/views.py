from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index(request):
    if 'id' not in request.session:
        return render(request, "DnD_app/index.html")
    return redirect("/profile")

def register(request):
    result = User.objects.validate_reg(request.POST)
    if result[0]:
        request.session['user_id'] = result[1].id
        request.session['user_name'] = result[1].name
        request.session['email'] = result[1].email
        return redirect("DnD_app/profile"))
    else:
        for error in result[1]: 
            messages.add_message(request, messages.INFO, error)
    return redirect(request, "/DnD_app/index")

def profile(request):
    return render(request.'DnD_app/profile.hhml/)

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
