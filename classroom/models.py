import os
from django.db import models
from utility.log import log
from utility.Exceptions import *
from utility.utils import GeneralUtils as GU

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

    studentId = models.CharField(max_length=255, primary_key=True, editable=False)
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
        response_dict = Student.objects.all()
        return response_dict

    @staticmethod
    def add_student(data):
        """

        @param data:
        @return:
        """
        userData = {}
        userData["firstname"] = GU.encrypt_data(data.get("firstName", ""))
        userData["lastname"] = GU.encrypt_data(data.get("lastName", ""))
        userData['password'] = GU.encrypt_data(data.get("password", ""))
        userData["gender"] = data.get("gender", "")
        userData["isActive"] = True
        obj = Student.objects.create(userData)
        return obj, True

    @staticmethod
    def check_student(student_id):
        """

        @param student_id:
        @return:
        """
        userData = Student.objects.filter(studnetId__exact=student_id)
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
            return

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
        userData["firstname"] = GU.encrypt_data(data.get("firstName", ""))
        userData["lastname"] = GU.encrypt_data(data.get("lastName", ""))
        userData['password'] = GU.encrypt_data(data.get("password", ""))
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
    isTeacherActive = models.BooleanField(default=True)

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
        user = StudnetTeacher.objects.get(teacherId=data["teacherId"], studentId=data['studentId'])
        if user is None:
            return

        user.isStarMarked = 1
        user.save()
        return data["teacherId"]