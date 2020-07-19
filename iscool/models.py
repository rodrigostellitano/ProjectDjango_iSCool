from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class StudentModel(models.Model):

    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    age = model.IntegerField()
    discipline = models.ManytoManyField(DisciplineModel)



class DisciplineModel(models.Model):

    discipline_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)



class AvaliationModel(models.Models):

    avaliation_id = models.IntegerField(primary_key=True)
    grade = models.IntegerField()
    semester = models.IntegerField()
    student_id = models.ForeignKey(StudentModel,null=False)
    discipline_id = models.ForeignKey(DisciplineModel,null=False)





    
