import uuid
from django.db import models
from django.contrib.auth import User
import datetime


groups_choices = (
    ("STAFF", "STAFF"),
    ("STUDENT", "STUDENT")
)


class Students(models.User):

    username = models.CharField(max_length = 50)
    email = models.CharField(max_length = 254)
    password = models.CharField(max_length = 50)
    groups = models.CharField(
        max_length = 10,
        choices =  groups_choices,
        )
    is_staff = False
    date_joined = models.DateField(auto_now = True, auto_now_add = False)



class Teacher(models.Model):
    dept = models.CharField(max_length = 50)
    t_first_name = models.CharField(max_length = 30)
    t_last_name = models.CharField(max_length = 30)
    teacher_id = models.IntegerField(primary_key = True, unique = True)



class Subject(models.Model):
    sname = models.CharField(max_length = 30)
    subject_id = models.AutoField(primary_key = True)
    teacher_id = models.ForeignKey(Teacher)
    teacher = models.ManyToManyField(Teacher)  # Defining the 'teaches' relation here.



class student(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    course = models.CharField(max_length = 40)
    semester = models.IntegerField()
    student_id = models.IntegerField()
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, ediatble = False)
    subject_id = models.ForeignKey(Subject)
    subject = models.ManyToManyField(Subject)   # Defining the 'studied' relation here.



class Attendance(models.Model):
    attendence_id = models.AutoField(primary_key = True)
    status = models.CharField(max_length = 2)
    date = models.DateField(auto_now = True, auto_now_add = False)
    student_id = models.ForeignKey(student, on_delete = models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete = models.CASCADE)
    #student = models.OneToOneField(student)  # Defining 'belongs' relationship since one studetn has only one attendance
    subject = models.ManyToManyField(Subject)
