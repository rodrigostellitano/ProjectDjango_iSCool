from django.db import models
from django.contrib.auth.models import User
from django.db.models import *
# Create your models here.





class DisciplineModel(models.Model):

    discipline_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)


class StudentModel(models.Model):

    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    discipline = models.ManyToManyField(DisciplineModel)




class AvaliationModel(models.Model):

    avaliation_id = models.IntegerField(primary_key=True)
    grade = models.IntegerField()
    semester = models.IntegerField()
    student_id = models.ForeignKey(StudentModel,null=False,on_delete=CASCADE)
    discipline_id = models.ForeignKey(DisciplineModel,null=False,on_delete=CASCADE)





    
