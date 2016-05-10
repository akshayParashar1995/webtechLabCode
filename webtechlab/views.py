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

dict = {}


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

	print(request.POST)
	email = request.POST.get("loginEmailName")
	password = request.POST.get("loginPwdName")
	user = auth.authenticate(username = email, password = password)
	if (user is not None):
		auth.login(request, user)
		stat = 1;
		if ('loginStudent' in request.POST):
			print("student")
			student=Student.objects.filter(user=user)
			if(len(student)==0):
				stat = "invalid username or password";
				return render(request,'login.html', {'status': stat})
			else:
				return displayContentStudent(request,user)
		else:
			print("teacher")
			teacher=Teacher.objects.filter(user=user)
			if(len(teacher)==0):
				stat = "invalid username or password";
				return render(request,'login.html', {'status': stat})		
			else:	
				return displayContentTeacher(request,user)
	else:		
		stat = "invalid username or password";
		return render(request,'login.html', {'status': stat})

 
def temp(request):

	return render(request,'temp.html',{
		"name": "Akshay",
		"subjects": ['Math','asdsd','sadsda']
	});

def editProfile(request):
	userId=request.GET.get("userid")
	print(userId)
	userLogged=User.objects.filter(id=userId)
	student = Student.objects.filter(user = userLogged[0])
	print(student[0])
	stat = 1;
	content = {'user':userLogged, 'student': student[0],'status': stat}

	return render(request, 'editProfile.html', {'content':content})


def saveEditProfile(request):
	print(request)
	username = request.POST.get("username")
	print(username)
	dob = request.POST.get("dob")
	print(dob)
	gender = request.POST.get("gender")
	print(gender)
	add = request.POST.get("address")
	print(add)
	email = request.POST.get("email")
	print(email)
	password = request.POST.get("pass")
	print(password)
	dept = request.POST.get("dept")
	print(dept)
	phone = request.POST.get("phone")
	print(phone)
	userid = request.POST.get("userid")
	print(userid)
	
	userLogged=User.objects.filter(id=userid)[0]
	student = Student.objects.filter(user = userLogged)[0]
	

	userLogged.set_password(password)
	userLogged.username=username
	userLogged.email=email
	userLogged.save()
	print(userLogged)

	student.phone_no=phone
	student.save()

	print(student.phone_no)
	print(userLogged.username)
	content = {'user':userLogged, 'student': student}


	return render(request, 'userprofile.html', {'content':content})


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
	isteacher=request.GET.get("isteacher")
	user = request.user
	# print(user)
	print(userId)
	print(viewall)
	print(isteacher)
	if(viewall==str(1)):
		courses=Course.objects.all()
	else:
		userLogged=User.objects.filter(id=userId)
		if(isteacher==str(1)):
			teacher = Teacher.objects.filter(user = userLogged[0])
			courses=teacher[0].teacher_course.all()
			print("teacher")
		else:
			student = Student.objects.filter(user = userLogged[0])
			courses=student[0].st_course.all()
			print("student")
	print(courses)
	content = {'courses':courses, 'user' : user,'isteacher':isteacher}
	return render(request, 'listOfCourses.html', { 'content' : content})



def openTest(request):
	testId = request.GET.get("testid")
	user = request.user
	test = Test.objects.filter(id = testId)
	arrofquestions = []
	questions = Questions.objects.all()
	# print(test[0].title)
	for i in questions:
		# print(i.test_id)
		if(str(i.test_id) == str(test[0].title)):
			arrofquestions.append(i)
	content={'test':test[0], 'arrofquestions': arrofquestions}
	user = request.user
	# print(test[0])
	# print(arrofquestions)
	return render(request, 'testWithSubmitButton.html', {'content':content, 'user':user})

def openDashboard(request):
	user = request.user
	return displayContent(request, user)

def displayContent(request,user):
	user=request.user
	student=Student.objects.filter(user=user)
	if(len(student)==0):
		return displayContentTeacher(request,user)
		print("teacher display")
	else:
		return displayContentStudent(request,user)
		print("student display")


def displayContentTeacher(request,user):
	teacher=Teacher.objects.filter(user=user)
	print(user.email)
	# courses=teacher[0].teacher_course.all()
	# print("details of teacher")
	# arrofdata = []

	# for i in courses:
	# 	temp = {}
	# 	temp['coursename'] = i.course_name
	# 	temp['notes'] = []
	# 	temp['assignment']= []
	# 	temp['test'] = []

	# 	notes = Notes.objects.filter(course_id = i.id)
	# 	for j in notes:
	# 		temp['notes'].append(j)

	# 	assign = Assignment.objects.filter(course_id = i.id)
	# 	for j in assign:
	# 		temp['assignment'].append(j)

	# 	testss = Test.objects.filter(course_id = i.id)
	# 	for j in testss:
	# 		temp['test'].append(j)

	# 	arrofdata.append(temp)
	# stat = 1;
	content = {'user':user, 'teacher': teacher[0]}
	print(content['teacher'])
	print(content.values())
	#print(content.teacher)
	# print(arrofdata)
	return render(request,'teacherDashBoard.html',{'content':content})

def displayContentStudent(request,user):
	student = Student.objects.filter(user = user)
	courses=student[0].st_course.all()
	arrofdata = []

	for i in courses:
		temp = {}
		temp['coursename'] = i.course_name
		temp['notes'] = []
		temp['assignment']= []
		temp['test'] = []

		notes = Notes.objects.filter(course_id = i.id)
		for j in notes:
			temp['notes'].append(j)

		assign = Assignment.objects.filter(course_id = i.id)
		for j in assign:
			temp['assignment'].append(j)

		testss = Test.objects.filter(course_id = i.id)
		for j in testss:
			temp['test'].append(j)

		arrofdata.append(temp)
	stat = 1;
	content = {'user':user, 'arrofdata': arrofdata,'status': stat}
	
	return render(request,'dashBoard.html',{'content':content})

def submitAnswer(request):
	# print(request)
	print(request.GET.get('qid'))
	print(request.GET.get('ansid'))
	qid = request.GET.get('qid')
	ansid = request.GET.get('ansid')
	question = Questions.objects.filter(id = qid)
	answers = Answers.objects.filter(question_id = question[0].id)
	print(answers[0].isCorrect)
	status = 0
	if( qid in dict):
		if( dict[qid] == 1):
			status = -1
			dict[qid] = 0
		elif(str(answers[0].isCorrect) == str(ansid)):
			status = 1
			dict[qid] = 1
		else:
			status = 0
	else:
		if(str(answers[0].isCorrect) == str(ansid)):
			dict[qid] = 1
			status = 1
		else:
			dict[qid] = 0
			status = 0

	temp = {
		'status': status,
		'length': len(dict)
	}
	return HttpResponse(json.dumps(temp), content_type="application/json")

def openNotesList(request):
	courseId = request.GET.get("courseid")
	course = Course.objects.filter(id = courseId)
	notes = Notes.objects.all()
	user = request.user
	# print(course[0].course_name)
	arrofnotes = []
	for i in notes:
		# print(i.course_id)
		if(str(i.course_id) == str(course[0].course_name)):
			arrofnotes.append(i)
	print(arrofnotes)
	content={'course':course[0], 'arrofnotes': arrofnotes, 'user':user}
	return render(request, 'listOfNotes.html', {'content':content})

def openNotes(request):
	notesId = request.GET.get("notesid")
	notes = Notes.objects.filter(id = notesId)
	user = request.user
	course = Course.objects.filter(course_name = notes[0].course_id)
	link = "/static/notes/" + str(notes[0].link) + ".pdf"
	content={'notes': notes[0], 'course':course[0], 'link' : link, 'user':user}
	return render(request, 'notes.html', {'content':content})
