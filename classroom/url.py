from django.conf.urls import url
from .views import *

urlpatterns = [
    # Student related URLs
    url(r'student/list', list_student),
    url(r'student/add', add_student),
    url(r'student/update', update_student),
    url(r'student/delete', delete_student_account),

    # Teacher related URLs
    url(r'teacher/list', list_teacher),
    url(r'teacher/add', add_teacher),
    url(r'teacher/update', update_teacher),
    url(r'teacher/delete', delete_teacher_account),
]