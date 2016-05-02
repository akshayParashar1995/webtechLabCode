from django.contrib import admin


# Register your models here.

from .models import *

admin.site.register(Student)

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Questions)
admin.site.register(Assignment)
admin.site.register(Notes)
admin.site.register(Answers)
admin.site.register(Video)
admin.site.register(Test)
# admin.site.register(StudentCourseRelation)
# admin.site.register(TeacherCourseRelation)
# admin.site.register(AssignmentCourseRelation)

