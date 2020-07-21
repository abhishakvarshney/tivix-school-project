import os
import json
import ast
import base64

from django.http import JsonResponse, HttpResponse
from classroom import models
from rest_framework.decorators import api_view, parser_classes
from django.shortcuts import render
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.response import Response
from utility.log import log
from utility.Exceptions import *
from utility.utils import GeneralUtils as GU


# Create your views here.
@api_view(['GET'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def list_student(request):
    if request.method == 'GET':
        response_dict = models.Student.list_student()
        if response_dict is None:
            response_dict = {}
            response_dict["status_code"] = 200
            response_dict["message"] = "No Student Available"
            response_dict["result"] = False
        else:
            response_dict['status_code'] = 200
            response_dict["result"] = True
        log.v('list student response = ' + str(response_dict))
        return Response(response_dict, status=201)


@api_view(['POST'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def add_student(request):
    data = json.loads(request.body.decode('utf-8'))
    response_dict = {}
    user_exist = models.Student.check_student(data.get('studentId', ''))
    log.error('UserCreation Status{}'.format(user_exist))
    if not user_exist:
        user_data, is_created = models.Student.add_user(data)
        response_dict['studentId'] = user_data.userId
        response_dict['status_code'] = 200
        return Response(response_dict, status=201)
    else:
        return Response({"status_code": 200, "message": "User Already Exists. Please Login"}, status=201)


@api_view(['PUT'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def update_student(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        if data.get('studentId', "") == "":
            raise ArgumentMissingException("Missing StudentID parameter")

        if data.get('firstName', "") == "" and data.get('lastName', "") == "" and data.get('gender', '') == '' and data.get('password', '') == '':
            raise ArgumentMissingException("Missing Student data parameter")

        student_id = models.Student.update_student(data)
        if student_id is None:
            response_dict = {}
            response_dict["status_code"] = 200
            response_dict["message"] = "Student not Found"
            response_dict["result"] = False
            log.d('[updateStudent]response = ' + str(response_dict))
        else:
            response_dict = {"studentId": student_id, "status_code": 200, "result": True}
            log.d('[updateStudent]response = ' + str(response_dict))
        return Response(response_dict, status=201)


@api_view(['POST'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def delete_student_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('studentId', "") == "":
            raise ArgumentMissingException("Missing studentId parameter")
        response_dict = {}
        try:
            models.Student.delete_student(data.get('studentId', ""))
            response_dict["status_code"] = 200
            response_dict["message"] = "Success"
            response_dict["result"] = True
        except Exception as ex:
            log.exception(ex)
            response_dict["status_code"] = 200
            response_dict["message"] = "Student Data not available"
            response_dict["result"] = False
        return response_dict


@api_view(['POST'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def student_delete_teacher(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('teacherId', "") == "":
            raise ArgumentMissingException("Missing TeacherId parameter")
        response_dict = {}
        try:
            models.StudentTeacherMapping.delete_teacher(data.get('teacherId', ""))
            response_dict["status_code"] = 200
            response_dict["message"] = "Success"
            response_dict["result"] = True
        except Exception as ex:
            log.exception(ex)
            response_dict["status_code"] = 200
            response_dict["message"] = "Teacher not linked with in Student Data"
            response_dict["result"] = False
        return response_dict


@api_view(['GET'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def list_teacher(request):
    if request.method == 'GET':
        response_dict = models.Teacher.list_teacher()
        if response_dict is None:
            response_dict = {}
            response_dict["status_code"] = 200
            response_dict["message"] = "No Teacher Available"
            response_dict["result"] = False
        else:
            response_dict['status_code'] = 200
            response_dict["result"] = True
        log.v('list teacher response = ' + str(response_dict))
        return Response(response_dict, status=201)


@api_view(['POST'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def add_teacher(request):
    data = json.loads(request.body.decode('utf-8'))
    response_dict = {}
    user_exist = models.Teacher.check_teacher(data.get('teacherId', ''))
    log.error('UserCreation Status{}'.format(user_exist))
    if not user_exist:
        user_data, is_created = models.Teacher.add_user(data)
        response_dict['teacherId'] = user_data.userId
        response_dict['status_code'] = 200
        return Response(response_dict, status=201)
    else:
        return Response({"status_code": 200, "message": "User Already Exists. Please Login"}, status=201)


@api_view(['POST'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def update_teacher(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        if data.get('teacherId', "") == "":
            raise ArgumentMissingException("Missing teacherID parameter")

        if data.get('firstName', "") == "" and data.get('lastName', "") == "" and data.get('gender', '') == '' and data.get('password', '') == '':
            raise ArgumentMissingException("Missing Teacher data parameter")

        teacher_id = models.Teacher.update_teacher(data)
        if teacher_id is None:
            response_dict = {}
            response_dict["status_code"] = 200
            response_dict["message"] = "Teacher not Found"
            response_dict["result"] = False
            log.d('[updateTeacher]response = ' + str(response_dict))
        else:
            response_dict = {"teacherId": teacher_id, "status_code": 200, "result": True}
            log.d('[updateTeacher]response = ' + str(response_dict))
        return Response(response_dict, status=201)


@api_view(['POST'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def delete_teacher_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('teacherId', "") == "":
            raise ArgumentMissingException("Missing teacherId parameter")
        response_dict = {}
        try:
            models.Teacher.delete_teacher(data.get('teacherId', ""))
            response_dict["status_code"] = 200
            response_dict["message"] = "Success"
            response_dict["result"] = True
        except Exception as ex:
            log.exception(ex)
            response_dict["status_code"] = 200
            response_dict["message"] = "Teacher Data not available"
            response_dict["result"] = False
        return response_dict


@api_view(['POST'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def teacher_delete_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('studentId', "") == "":
            raise ArgumentMissingException("Missing studentId parameter")
        response_dict = {}
        try:
            models.StudentTeacherMapping.delete_student(data.get('studentId', ""))
            response_dict["status_code"] = 200
            response_dict["message"] = "Success"
            response_dict["result"] = True
        except Exception as ex:
            log.exception(ex)
            response_dict["status_code"] = 200
            response_dict["message"] = "Student not linked with in Teacher Data"
            response_dict["result"] = False
        return response_dict


@api_view(['POST'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def mark_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('studentId', "") == "" or data.get('teacherId', "") == "":
            raise ArgumentMissingException("Missing teacherId or studentId parameter")
        response_dict = {}
        teacher_id = models.StudentTeacherMapping.mark_student_by_teacher(data)
        if teacher_id not in [None, '']:
            response_dict["status_code"] = 200
            response_dict["message"] = "Success"
            response_dict["result"] = True
        else:
            response_dict["status_code"] = 200
            response_dict["message"] = "Student not linked with in Teacher Data"
            response_dict["result"] = False
        return response_dict


@api_view(['POST'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def unmark_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('studentId', "") == "" or data.get('teacherId', "") == "":
            raise ArgumentMissingException("Missing teacherId or studentId parameter")
        response_dict = {}
        teacher_id = models.StudentTeacherMapping.unmark_student_by_teacher(data)
        if teacher_id not in [None, '']:
            response_dict["status_code"] = 200
            response_dict["message"] = "Success"
            response_dict["result"] = True
        else:
            response_dict["status_code"] = 200
            response_dict["message"] = "Student not linked with in Teacher Data"
            response_dict["result"] = False
        return response_dict


@api_view(['POST'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def add_teacher_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('studentId', "") == "" or data.get('teacherId', "") == "":
            raise ArgumentMissingException("Missing teacherId or studentId parameter")
        response_dict = {}
        try:
            models.StudentTeacherMapping.add_student_teacher(data)
            response_dict["status_code"] = 200
            response_dict["message"] = "Success"
            response_dict["result"] = True
        except Exception as ex:
            log.exception(ex)
            response_dict["status_code"] = 200
            response_dict["message"] = "Data Not available."
            response_dict["result"] = False
        return response_dict
