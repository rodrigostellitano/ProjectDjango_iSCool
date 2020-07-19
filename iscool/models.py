from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models import *
# Create your models here.





class DisciplineModel(models.Model):

    discipline_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class StudentModel(models.Model):

    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    age = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(20)])
    discipline = models.ManyToManyField(DisciplineModel, blank=True)

    def __str__(self):
        return self.name



class AvaliationModel(models.Model):
    SEMESTER = (
        ('1','1º Semestre'),
        ('2','2º Semestre'),
        ('3','3º Semestre'),
        
    )

    avaliation_id = models.IntegerField(primary_key=True)
    semester = models.CharField(max_length=10,
                                choices=SEMESTER)
    note = models.FloatField(validators=[MaxValueValidator(10.0),MinValueValidator(0.0)])
    student_id = models.ForeignKey(StudentModel,null=False,on_delete=CASCADE)
    discipline_id = models.ForeignKey(DisciplineModel,null=False,on_delete=CASCADE)
 




    
