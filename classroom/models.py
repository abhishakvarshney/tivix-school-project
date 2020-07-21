from django.db import models
from utility.log import log
from utility.Exceptions import *

# Create your models here.
GENDER_MALE = 'Male'
GENDER_FEMALE = 'Female'

GENDER_CHOICES = (
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female'),
)


class Student(models.Model):
    """
    @return:
    """

    class Meta:
        """
        @return:
        """
        db_table = 'student'

    studentId = models.CharField(max_length=255, primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.TextField(null=True, blank=True)
    lastname = models.TextField(null=True, blank=True)
    isActive = models.BooleanField(default=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=GENDER_MALE)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "{} {}".format(self.lastname, self.firstname)

    @staticmethod
    def add_student(data):
        """

        @param data:
        @return:
        """
        userData = {}
        userData['firstname'] = User.encrypt_data(data.get(DB.User.FIRST_NAME, ''))
        userData['lastname'] = User.encrypt_data(data.get(DB.User.LAST_NAME, ''))
        userData['gender'] = data.get(DB.User.GENDER, '')
        userData['isActive'] = True
        obj = User.objects.create(userData)
        return obj, True

    @staticmethod
    def update_student(data):
        """

        @param data:
        @return:
        """
        user = User.objects.get(userId=data['studentId'])
        if user is None:
            return
        attrDict = {}
        # ToDo: Check for types

        if data.get('firstName', '') != '':
            user.firstname = GU.encryptData(data['firstName'])
        if data.get('lastName', '') != '':
            user.lastname = GU.encryptData(data['lastName'])
        if data.get('gender', '') != '':
            user.gender = data['gender']

        user.save()
        return data['studentId']
    
    @staticmethod
    def delete_user(user_id):
        """

        @param user_id:
        """
        user = User.objects.get(userId=user_id)
        user.isActive = 0
        user.save()