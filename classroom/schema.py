import graphene

from graphene_django.types import DjangoObjectType

from classroom.models import Student, Teacher, StudentTeacherMapping


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher


class StudentTeacherMappingType(DjangoObjectType):
    class Meta:
        model = StudentTeacherMapping

class Query(object):
    all_student = graphene.List(StudentType)
    all_teacher = graphene.List(TeacherType)
    all_studentteachermapping = graphene.List(StudentTeacherMappingType)

    def resolve_all_student(self, info, **kwargs):
        return Student.objects.all()

    def resolve_all_teacher(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Teacher.objects.all()

    def resolve_all_studentteachermapping(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return StudentTeacherMapping.objects.all()
