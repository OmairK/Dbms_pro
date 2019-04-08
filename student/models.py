import uuid
from django.db import models
import datetime
from django.contrib.auth import User 

groups_Choice = (
    ("STAFF","STAFF"),
    ("STUDENT","STUDENT")
)

class Students(models.User):

    username = models.CharField(max_lenght = 50)
    email = models.EmailField(max_length=254)
    password = models.CharField( max_length=50)
    groups = models.CharField(
        max_length = 10,
        choices = groups_Choice,
        )
    is_staff = False
    date_joined = models.DateField(auto_now=True, auto_now_add=False)   

class Teacher(models.Model):
    dept = models.CharField(max_length=50)
    t_first_name =  models.CharField(max_length=30)
    t_last_name = models.CharField(max_length=30)

class subject(models.Model):
    sname = models.CharField(max_length=30)
    teac_id = models.ForeignKey(Teacher)
    subject_id = models.AutoField(primary_key = True)

    
class students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    course = models.CharField(max_lenght=40)
    student_id = models.CharField(max_length = 30)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    semester = models.IntegerField()
    # atted_id = models.ForeignKey(attendance)
    subject_id = models.ForeignKey(subject)

  



    # teacher_dept = models.ManyToManyField("app.Model", verbose_name=_(""))
  
class attendance(models.Model):
    attendance_id = models.AutoField(primary_key =True)
    date = models.DateField(auto_now=True, auto_now_add=False)
    status = models.CharField(max_length=2)
    stud_id = models.ForeignKey(students, on_delete=models.CASCADE)
    subj_id = models.ForeignKey(subject, on_delete=models.CASCADE)
    # teach_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)


