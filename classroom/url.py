from django.conf.urls import url
from .views import *

urlpatterns = [
    # Student related URLs
    url(r'list/student/', list_student),
    url(r'add/student/', add_student),
    url(r'update/student/', update_student),
    url(r'delete/student/', delete_student_account),

    # Teacher related URLs
    url(r'list/teacher', list_teacher),
    url(r'add/teacher', add_teacher),
    url(r'update/teacher', update_teacher),
    url(r'delete/teacher', delete_teacher_account),

    # Teacher Student related URLs
    url(r'remove/teacherFromStudentList', student_delete_teacher),
    url(r'remove/studentFromTeacherList', teacher_delete_student),
    url(r'mark/student', mark_student),
    url(r'add/studentTeacher', add_teacher_student),
    url(r'unmarking/student', unmark_student),
]