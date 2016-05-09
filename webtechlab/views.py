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
def signUp(request):
	#print(request.POST.get("nameSignup"));
	#print(request.POST.get("rollnoSignup"));
	#print(request.POST.get("batchSignup"));
	#print(request.POST.get("optradio"));
	print(request.POST.get("emailSignup"));
	print(request.POST.get("pwdSignup"));
	userSigningUp=User(username = request.POST.get("emailSignup"), is_active=True)
	userSigningUp.set_password(request.POST.get("pwdSignup"))
	userSigningUp.save()
	student=Student(user=userSigningUp,rollno=request.POST.get("rollnoSignup"),year=2,dob=datetime.datetime.now(),phone_no=9911991199)
	student.save()

	user = auth.authenticate(username = request.POST.get("emailSignup"), password = request.POST.get("pwdSignup"))
	print(user)
	if (user is not None):
		auth.login(request, user)
		stat = 1;
		return displayContent(request,user)
		# content = {'user': user,'status': stat}
		# return render(request,'dashBoard.html',{'content':content})
	else:		
		stat = "invalid username or password";
		return render(request,'login.html', {'status': stat})

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
	else:		
		stat = "invalid username or password";
		return render(request,'login.html', {'status': stat})

 
def temp(request):

	return render(request,'temp.html',{
		"name": "Akshay",
		"subjects": ['Math','asdsd','sadsda']
	});

def openProfile(request):
	userId=request.GET.get("userid")
	print(userId)
	userLogged=User.objects.filter(id=userId)
	student = Student.objects.filter(user = userLogged[0])
	print(student[0])
	stat = 1;
	content = {'user':userLogged, 'student': student[0],'status': stat}


	return render(request, 'userprofile.html', {'content':content})

def openCourses(request):
	userId=request.GET.get("userid")
	viewall=request.GET.get("viewall")
	print(userId)
	print(viewall)
	if(viewall==str(1)):
		courses=Course.objects.all()
	else:
		userLogged=User.objects.filter(id=userId)
		student = Student.objects.filter(user = userLogged[0])
		courses=student[0].st_course.all()
	print(courses)
	return render(request, 'listOfNotes.html', {'courses':courses})



def openTest(request):
	testId = request.GET.get("testid")
	
	test = Test.objects.filter(id = testId)
	arrofquestions = []
	questions = Questions.objects.all()
	# print(test[0].title)
	for i in questions:
		# print(i.test_id)
		if(str(i.test_id) == str(test[0].title)):
			arrofquestions.append(i)
	content={'test':test[0], 'arrofquestions': arrofquestions}
	# print(test[0])
	print(arrofquestions)
	return render(request, 'testWithSubmitButton.html', {'content':content})


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
