from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
from random import *
import math

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
    games = Game.objects.all()
    return render(request,'DnD_app/profile.html', {'games':games})

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

def character(request):
    characters = Character.objects.all()
    return render(request, "DnD_app/character.html",{'characters':characters})

def save(request,id):
    active = Game.objects.active_game(request.session['id'])
    if active[0] == False:
        user= User.objects.get(id=request.session['id'])
        character= Character.objects.get(id=id)
        game= Game.objects.create(user = user, hp = request.session['hp'], gold=request.session['gold'], level=request.session['level'], character=character)
    else:
        for active_game in active[1]: 
            game = Game.objects.get(id=active_game.id)
            game.character = Character.objects.get(id=id)
            game.hp = request.session['hp']
            game.gold = request.session['gold']
            game.level = request.session['level']
            game.save()
    return redirect('/profile')

def restart(request):
    del request.session['gold']
    del request.session['hp']
    del request.session['level']
    return redirect ('/profile')

def keep_playing(request):
    return render(request, "DnD_app/game.html")

def new_game(request, id):
    character = Character.objects.get(id=id)
    request.session['hp'] = character.hp
    request.session['gold'] = character.gold
    request.session['level'] = 1
    story = Story.objects.get(id=request.session['level'])
    return render(request, "DnD_app/game.html", {'character':character, 'story' : story})

def game(request):
    game = Game.objects.get(user=request.session['id'])
    character= game.character
    story = Story.objects.get(id=request.session['level'])
    return render(request, "DnD_app/game.html", {'character':character, 'story' : story})

def end(request):
    return render(request, "DnD_app/end.html")

def game_over(request):
    return render(request, "DnD_app/game_over.html")

def first (request):
    dice = randint (1, 20)
    request.session["dice"]=dice
    game = Game.objects.get(user=request.session['id'])
    if game.character.id == 1:
        dice +=4
        request.session["dice"]=dice
    if dice >= 14:
        request.session['level']+=1
        request.session['gold']+=(dice-9)
        if request.session['level'] >6:
            return redirect ('/end')
        messages.info(request, 'You have rolled the number :{}'.format(dice))
        messages.info(request, 'You have reached the next level')
        return redirect ('/game')
    else:
        request.session['hp'] -= (20-dice)
        if request.session['hp'] <= 0:
            return redirect ('/game_over')
        messages.info(request, 'You have rolled the number :{}'.format(dice))
        return redirect ('/game')

def second (request):
    dice = randint (1, 20)
    request.session["dice"]=dice
    game = Game.objects.get(user=request.session['id'])
    if game.character.id == 2:
        dice +=4
        request.session["dice"]=dice
    if dice >= 14:
        request.session['level']+=1
        request.session['gold']+=(dice-9)
        if request.session['level']>6:
            return redirect ('/end')
        messages.info(request, 'You have rolled the number :{}'.format(dice))
        messages.info(request, 'You have reached the next level')
        return redirect ('/game')
    else:
        request.session['hp'] -= (20-dice)
        if request.session['hp'] <= 0:
            return redirect ('/game_over')
        messages.info(request, 'You have rolled the number :{}'.format(dice))    
        return redirect ('/game')

def third (request):
    dice = randint (1, 20)
    request.session["dice"]=dice
    game = Game.objects.get(user=request.session['id'])
    if dice >= 14:
        request.session['level']+=1
        request.session['gold'] = request.session['gold']+int(math.floor((dice-9)*1.5))
        if request.session['level']>6:
            return redirect ('/end')
        messages.info(request, 'You have rolled the number :{}'.format(dice))
        messages.info(request, 'You have reached the next level')
        return redirect ('/game')
    else:
        request.session['hp'] -= (20-dice)
        if request.session['hp'] <= 0:
            return redirect ('/game_over')
        messages.info(request, 'You have rolled the number :{}'.format(dice))
        return redirect ('/game')
