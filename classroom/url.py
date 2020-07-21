from django.conf.urls import url
from .views import *

urlpatterns = [
    # Student related URLs
    url(r'student/list', ),
    url(r'student/add', ),
    url(r'student/update', ),
    url(r'student/delete', ),
    # Teacher related URLs
    url(r'teacher/list', ),
    url(r'teacher/add', ),
    url(r'teacher/update', ),
    url(r'teacher/delete', ),
]