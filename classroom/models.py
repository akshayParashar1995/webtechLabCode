from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
	# course_id=models.IntegerField(max_length=8)
	course_name=models.CharField(max_length=30)
	duration=models.IntegerField(max_length=4)
	course_fee=models.IntegerField(max_length=6)
	def __str__(self):
	    return self.course_name;

class Student(models.Model):
	# student_id=models.IntegerField(max_length=8)
	# student_name=models.CharField(max_length=30)
	user = models.OneToOneField(User)
	dob=models.DateField()
	phone_no=models.BigIntegerField(max_length=10)
	st_course = models.ManyToManyField(Course)
	def __str__(self):
	    return "dob:"+str(self.dob);
	
class Teacher(models.Model):
	# teacher_id=models.IntegerField(max_length=8)
	# teacher_name=models.CharField(max_length=30)
	user = models.OneToOneField(User)
	department=models.CharField(max_length=20)
	phone_no=models.BigIntegerField(max_length=10)
	teacher_course = models.ManyToManyField(Course)

	def __str__(self):
	    return self.user.username;
	
	
# class StudentCourseRelation(model.Model):
#     student_id=models.ForeignKey('Student')
#     course_id=models.ForeignKey('Course')
	
# class TeacherCourseRelation(model.Model):
#     teacher_id=models.ForeignKey('Teacher')
#     course_id=models.ForeignKey('Course')
	
class Assignment(models.Model):
	# assignment_id=models.IntegerField(max_length=8)
	date_of_submission=models.DateTimeField()
	def __str__(self):
	    return self.assignment_id;
		
class Notes(models.Model):
	# note_id=models.IntegerField(max_length=8)
	course_id=models.ForeignKey(Course)
	teacher_id=models.ForeignKey(Teacher)
	date=models.DateTimeField()
	title=models.CharField(max_length=10)
	def __str__(self):
		return self.title;
	
	
class Questions(models.Model):
	# question_id=models.IntegerField(max_length=8)
	# answer_id=models.IntegerField(max_length=8)
	question_text=models.CharField(max_length=120)

class Answers(models.Model):
	answer_text = models.CharField(max_length = 255)
	question_id = models.ForeignKey(Questions)
	isCorrect = models.BooleanField(default = 0)

class Video(models.Model):
	course_id=models.ForeignKey(Course)
	teacher_id=models.ForeignKey(Teacher)
	date=models.DateTimeField()
	title=models.CharField(max_length=10)
	# path 
	description = models.CharField(max_length = 255)	
