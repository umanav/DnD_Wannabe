from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager (models.Manager):
    def valid_registration (self,postData):
        errors = []
        first_name = postData['first_name']
        last_name = postData['last_name']
        username = postData['username']
        email = postData['email']
        password = postData['password']
        pwd_confirm = postData['pwd_confirm']
        if len(first_name) ==0  :
            errors.append ("Your first name is required")
        elif len(first_name) < 3:
            errors.append ("Your first name should be at least 3 characters long")
        if len(last_name) ==0  :
            errors.append ("Your last name is required")
        elif len(last_name) < 3:
            errors.append ("Your last name should be at least 3 characters long")
        if len(username) == 0:
            errors.append ("Your username is required")
        elif len(username) < 3:
            errors.append ("Your username should be at least 3 characters long")
        if len(email) == 0:
            errors.append ("Your email is required")
        elif not EMAIL_REGEX.match(postData['email']):
           errors.append ('Please enter a valid email address.')
        if len(password) == 0:
            errors.append ("Your password is required")
        elif len(password) < 8:
            errors.append ("Your Password must be at least 8 characters long")
        if User.objects.filter(username = username):
            errors.append ('This username is already in use. Please log in instead.')
        if password != pwd_confirm:
            errors.append ('The password and password confirmation must match')
        if errors == []:
            result = User.objects.filter(username=username)
            if len(result)>0:
                errors.append("Username already exists ")
                return (errors,True)
            else:
                password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                user = User.objects.create(first_name =first_name, last_name = last_name, username =username, email = email, password = password)
                return (user,False)
        return (errors,True)

    def valid_login(self,postData):
        errors =[]
        username = postData['username']
        password = postData['password']
        if len(username) == 0:
            errors.append ("Your username is required")
        elif len(username) < 3:
            errors.append ("Your username should be at least 3 characters long")
        if len(password) == 0:
            errors.append ("Please enter your password")
        try:
            user = User.objects.get(username = username)
            if bcrypt.checkpw ( password.encode(), user.password.encode() ):
                return errors
            errors.append ("Invalid username/password combination")
        except User.DoesNotExist:
            errors.append ("Invalid username/password combination")
        return errors

class GameManager(models.Manager):
    def active_game(self,id):
        user = User.objects.get(id=id)
        active_game = Game.objects.filter(user = user)
        if len(active_game) == 0:
            return (False,active_game)
        return (True,active_game) 


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Character(models.Model):
    name = models.CharField(max_length=255)
    hp = models.IntegerField()
    gold = models.IntegerField()
    user = models.ManyToManyField(User, related_name = 'Characters')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image_route = models.CharField(max_length=255, default="img", null=True, blank=True)

class Game(models.Model):
    user = models.ForeignKey(User, related_name = 'User')
    hp = models.IntegerField()
    gold = models.IntegerField()
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = GameManager()