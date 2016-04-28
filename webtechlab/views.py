from django.contrib import auth
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import json
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils import timezone
from django.db.models import Q
from django.core import serializers
from classroom.models import *
from urllib.request import urlopen
import base64
import requests
import datetime
import os
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate

# Create your views here.
def login(request):

    return render(request,'login.html',{
	'hello':"hey"
    });
        

def loginCredentials(request):
    
    print(request.GET.get("email"));
    print(request.GET.get("pwd"));
	
    #user =  User.objects.filter(email=request.GET.get("email"), password=request.GET.get("pwd"))
    #if user is not None:
    exists=User.objects.filter(email=request.GET.get("email"), password=request.GET.get("pwd")).exists();
    if exists:
    # the password verified for the user
        print("The password is valid")
        stat=1;
    else:
    # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
        stat=0;
    
    return HttpResponse(json.dumps({'status':stat}), content_type="application/json")
        
def temp(request):

    return render(request,'temp.html',{
	    "name": "Akshay",
        "subjects": ['Math','asdsd','sadsda']
    });


