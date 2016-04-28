from django.contrib import admin


# Register your models here.

from .models import Course,Student,User

admin.site.register(Student)

admin.site.register(Course)


