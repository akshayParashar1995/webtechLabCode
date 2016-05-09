from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
	#course_id=models.IntegerField(max_length=8,editable=False)
	course_name=models.CharField(max_length=30)
	duration=models.IntegerField()
	course_fee=models.IntegerField()
	def __str__(self):
		return self.course_name;

class Student(models.Model):
	#studentt_id=models.IntegerField(max_length=8,editable=False)
	user = models.OneToOneField(User)
	dob=models.DateField()
	rollno=models.CharField(max_length=20)
	year=models.IntegerField()
	phone_no=models.BigIntegerField()
	st_course = models.ManyToManyField(Course)
	def __str__(self):
		return "dob:"+str(self.dob);
	
class Teacher(models.Model):
	#teacher_id=models.IntegerField(max_length=8,default=0,editable=False)
	user = models.OneToOneField(User)
	department=models.CharField(max_length=20)
	phone_no=models.BigIntegerField()
	teacher_course = models.ManyToManyField(Course)

	def __str__(self):
		return self.user.username;
	
	
# class StudentCourseRelation(models.Model):
	# type = models.CharField
#     student_id=models.ForeignKey('Student',editable=False)
#     course_id=models.ForeignKey('Course',editable=False)
	
# class TeacherCourseRelation(models.Model):
#     teacher_id=models.ForeignKey('Teacher',editable=False)
#     course_id=models.ForeignKey('Course',editable=False)
	
class Assignment(models.Model):
	#assignment_id=models.IntegerField(max_length=8,default=0,editable=False)
	date_of_submission=models.DateTimeField()
	course_id=models.ForeignKey(Course)
	title = models.CharField(max_length = 200)
	def __str__(self):
		return self.title;
	

# class AssignmentCourseRelation(models.Model):
#     teacher_id=models.ForeignKey('Assignment')
#     course_id=models.ForeignKey('Course')

class Notes(models.Model):
	#note_id=models.IntegerField(max_length=8,default=0,editable=False)
	course_id=models.ForeignKey(Course)
	teacher_id=models.ForeignKey(Teacher)
	date=models.DateTimeField()
	title=models.CharField(max_length=100)
	def __str__(self):
		return self.title;
	

class Test(models.Model):
	course_id = models.ForeignKey(Course)
	title = models.CharField(max_length=120)
	date_of_test=models.DateTimeField()
	max_marks=models.IntegerField()
	duration=models.IntegerField()
	def __str__(self):
		return self.title;
	
class Questions(models.Model):
	#question_id=models.IntegerField(max_length=8,default=0,editable=False)
	test_id = models.ForeignKey(Test)
	question_text=models.CharField(max_length=120)
	answer1 = models.CharField(max_length=120)
	answer2 = models.CharField(max_length=120)
	answer3 = models.CharField(max_length=120)
	answer4 = models.CharField(max_length=120)
	def __str__(self):
		return self.question_text;

class Answers(models.Model):
	#answer_id=models.IntegerField(max_length=8,default=0,editable=False)
	question_id = models.ForeignKey(Questions)
	isCorrect = models.IntegerField()
	def __str__(self):
		return str(self.question_id);




class Video(models.Model):
	course_id=models.ForeignKey(Course)
	teacher_id=models.ForeignKey(Teacher)
	date=models.DateTimeField()
	title=models.CharField(max_length=100)
	# path 
	description = models.CharField(max_length = 255)	
	def __str__(self):
		return self.title;
