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
import base64
import requests
import datetime
import os
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.decorators.http import require_POST
from django.contrib import auth

# Create your views here.
def login(request):

	return render(request,'login.html',{
	'hello':"hey"
	});
		

def loginCredentials(request):

	email = request.POST.get("loginEmailName")
	password = request.POST.get("loginPwdName")
	# print(email)
	# print(password)
	user = auth.authenticate(username = email, password = password)
	# print(user)
	# print(user)
	if (user is not None):
		auth.login(request, user)
		stat = 1;
		return displayContent(request,user)
		# content = {'user': user,'status': stat}
		# return render(request,'dashBoard.html',{'content':content})
	else:		
		stat = "invalid username or password";
		return render(request,'login.html', {'status': stat})

	# print(request.POST.get("loginEmailName",''));
	# print(request.POST.get("loginPwdName",''));
	
	# #user =  User.objects.filter(email=request.GET.get("email"), password=request.GET.get("pwd"))
	# #if user is not None:
	# user_info=User.objects.filter(email=request.POST.get("loginEmailName",''), password=request.POST.get("loginPwdName",''))
	# print(User.objects.all())
	# print(User.objects.filter(password=request.POST.get("loginPwdName",'')))

	# if len(user_info)>0:
	# # the password verified for the user
	# 	print("The password is valid")
	# 	stat=1;
	# 	content={'user':user_info,'status':stat}
	# 	return render(request,'dashBoard.html',{'content':content})
	# else:
	# # the authentication system was unable to verify the username and password
	# 	print("The username and password were incorrect.")
	# 	stat="invalid username or password";
	# 	return render(request,'login.html',{'status':stat})
 
def temp(request):

	return render(request,'temp.html',{
		"name": "Akshay",
		"subjects": ['Math','asdsd','sadsda']
	});

def displayContent(request,user):
	student = Student.objects.filter(user = user)
	print(student[0].st_course.all())
	courses=student[0].st_course.all()
	arrofdata = []

	for i in courses:
		temp = {}
		temp['coursename'] = i.course_name
		temp['notes'] = []
		temp['assignment']= []
		temp['test'] = []

		print(Notes.objects.filter(course_id = i.id))
		notes = Notes.objects.filter(course_id = i.id)
		for j in notes:
			temp['notes'].append(j)

		print(Assignment.objects.filter(course_id = i.id))
		assign = Assignment.objects.filter(course_id = i.id)
		for j in assign:
			temp['assignment'].append(j)

		print(Test.objects.filter(course_id = i.id))
		testss = Test.objects.filter(course_id = i.id)
		for j in testss:
			temp['test'].append(j)

		arrofdata.append(temp)
	print("arrofdata::::                 ")
	print(arrofdata)
	stat = 1;
	content = {'user':user, 'arrofdata': arrofdata,'status': stat}
	
	return render(request,'dashBoard.html',{'content':content})

