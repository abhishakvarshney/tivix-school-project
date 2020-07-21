import os
import uuid
import json
from django.db import models
from utility.log import log
from utility.Exceptions import *
from utility.utils import GeneralUtils as GU
from django.http import JsonResponse
from django.core import serializers


# Create your models here.
__all__ = ["Student", "Teacher", "StudentTeacherMapping"]

GENDER_MALE = "Male"
GENDER_FEMALE = "Female"

GENDER_CHOICES = (
    (GENDER_MALE, "Male"),
    (GENDER_FEMALE, "Female"),
)


class Student(models.Model):
    """
    @return:
    """

    class Meta:
        """
        @return:
        """
        db_table = "student"

    studentId = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=45, null=False, blank=False)
    firstname = models.TextField(null=True, blank=True)
    lastname = models.TextField(null=True, blank=True)
    isActive = models.BooleanField(default=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=GENDER_MALE)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "{} {}".format(self.lastname, self.firstname)

    @staticmethod
    def list_student():
        """
        @return:
        """
        response_dict = json.loads(serializers.serialize('json', Student.objects.all()))
        student_data_list = []
        print(response_dict)
        for data in response_dict:
                student_data = {}
                student_data['studentId'] = data['fields']['studentId']
                student_data['firstName'] = GU.decryptData(data['fields']['firstname'])
                student_data['lastName'] = GU.decryptData(data['fields']['lastname'])
                student_data['gender'] = data['fields']['gender']
                student_data_list.append(student_data)
        return student_data_list

    @staticmethod
    def add_student(data):
        """

        @param data:
        @return:
        """
        user = Student()
        user.studentId = data.get("studentId", "")
        user.firstname = GU.encryptData(data.get("firstName", ""))
        user.lastname = GU.encryptData(data.get("lastName", ""))
        user.password = GU.encryptData(data.get("password", ""))
        user.gender = data.get("gender", "")
        user.isActive = True
        if Student.check_student(data.get('studentId')) is None:
            user.save()
            return user, True
        return user, False

    @staticmethod
    def check_student(student_id):
        """

        @param student_id:
        @return:
        """
        userData = Student.objects.filter(studentId__exact=student_id)
        if userData is None or len(userData) == 0:
            return None
        return userData[0]

    @staticmethod
    def update_student(data):
        """

        @param data:
        @return:
        """
        user = Student.objects.get(studentId=data["studentId"])
        if user is None:
            return None

        if data.get("firstName", "") != "":
            user.firstname = GU.encryptData(data["firstName"])
        if data.get("lastName", "") != "":
            user.lastname = GU.encryptData(data["lastName"])
        if data.get("gender", "") != "":
            user.gender = data["gender"]
        if data.get("password", "") != "":
            user.password = GU.encryptData(data["password"])

        user.save()
        return data["studentId"]

    @staticmethod
    def delete_student(student_id):
        """

        @param student_id:
        """
        student = Student.objects.get(studentId=student_id)
        student.isActive = 0
        student.save()


class Teacher(models.Model):
    """
    @return:
    """

    class Meta:
        """
        @return:
        """

        db_table = "teacher"

    teacherId = models.CharField(max_length=255, primary_key=True, editable=False)
    password = models.CharField(max_length=45, null=False, blank=False)
    firstname = models.TextField(null=True, blank=True)
    lastname = models.TextField(null=True, blank=True)
    isActive = models.BooleanField(default=True)
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, default=GENDER_MALE
    )
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "{} {}".format(self.lastname, self.firstname)

    @staticmethod
    def list_teacher():
        """

        @return:
        """
        response_dict = Teacher.objects.all()
        return response_dict

    @staticmethod
    def check_teacher(teacher_id):
        """

        @param teacher_id:
        @return:
        """
        userData = Teacher.objects.filter(teacherId__exact=teacher_id)
        if userData is None or len(userData) == 0:
            return None
        return userData[0]

    @staticmethod
    def add_teacher(data):
        """

        @param data:
        @return:
        """
        userData = {}
        userData["firstname"] = GU.encryptData(data.get("firstName", ""))
        userData["lastname"] = GU.encryptData(data.get("lastName", ""))
        userData['password'] = GU.encryptData(data.get("password", ""))
        userData["gender"] = data.get("gender", "")
        userData["isActive"] = True
        obj = Teacher.objects.create(userData)
        return obj, True

    @staticmethod
    def update_teacher(data):
        """

        @param data:
        @return:
        """
        user = Teacher.objects.get(teacherId=data["teacherId"])
        if user is None:
            return

        if data.get("firstName", "") != "":
            user.firstname = GU.encryptData(data["firstName"])
        if data.get("lastName", "") != "":
            user.lastname = GU.encryptData(data["lastName"])
        if data.get("gender", "") != "":
            user.gender = data["gender"]

        user.save()
        return data["teacherId"]

    @staticmethod
    def delete_teacher(teacher_id):
        """

        @param teacher_id:
        """
        user = Teacher.objects.get(teacherId=teacher_id)
        user.isActive = 0
        user.save()


class StudentTeacherMapping(models.Model):
    """
    @return:
    """

    class Meta:
        """
        @return:
        """

        db_table = "student_teacher"

    mapId = models.CharField(max_length=255, primary_key=True, default=uuid.uuid4, editable=False)
    teacherId = models.ForeignKey(Teacher, on_delete=models.PROTECT, db_column="teacherId")
    studentId = models.ForeignKey(Student, on_delete=models.PROTECT, db_column="studentId")
    isStarMarked = models.BooleanField(default=False)
    isStudentActive = models.BooleanField(default=True)


    @staticmethod
    def delete_student(student_id):
        """

        @param student_id:
        """
        student = StudentTeacher.objects.get(studentId=student_id)
        student.isStudentActive = 0
        student.save()

    @staticmethod
    def delete_teacher(teacher_id):
        """

        @param student_id:
        """
        teacher = StudentTeacher.objects.get(teacherId=teacher_id)
        teacher.isTeacherActive = 0
        teacher.save()

    @staticmethod
    def mark_student_by_teacher(data):
        """

        @param data:
        @return:
        """
        user = StudentTeacher.objects.get(teacherId=data["teacherId"], studentId=data['studentId'])
        if user is None:
            return

        user.isStarMarked = 1
        user.save()
        return data["teacherId"]

    @staticmethod
    def unmark_student_by_teacher(data):
        """

        @param data:
        @return:
        """
        user = StudentTeacher.objects.get(teacherId=data["teacherId"], studentId=data['studentId'])
        if user is None:
            return

        user.isStarMarked = 0
        user.save()
        return data["teacherId"]

    @staticmethod
    def add_student_teacher(data):
        """

        @param student_id:
        """
        student = StudentTeacher.objects.get(studentId=data.get('studentId'), teacherId=data.get('teacherId'))
        student.isStudentActive = 1
        student.save()
