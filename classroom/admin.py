from django.contrib import admin
from classroom.models import Student, Teacher, StudentTeacherMapping
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(StudentTeacherMapping)