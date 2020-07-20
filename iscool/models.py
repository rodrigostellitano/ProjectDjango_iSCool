from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models import *


"""
TASK
- Run o auto increment 1000 na tabela StudentModel


"""
class DisciplineModel(models.Model):

    discipline_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class StudentModel(models.Model):

        # INSERT IN THE DB TO STUDENT_ID START 1000: ALTER TABLE iscool_studentmodel AUTO_INCREMENT = 1000;
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    age = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(20)])
       
    def __str__(self):
        return self.name

     #I stopped using that form and created the relationship table manually
    #discipline = models.ManyToManyField(DisciplineModel, blank=True)



class Student_has_Discipline(models.Model):

    student_has_discipline_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(StudentModel,on_delete=models.CASCADE)
    discipline_id = models.ForeignKey(DisciplineModel, on_delete=models.CASCADE)


class AvaliationModel(models.Model):
    SEMESTER = (
        ('1','1º Semestre'),
        ('2','2º Semestre'),
        ('3','3º Semestre'),
        
    )
        
    avaliation_id = models.AutoField(primary_key=True)
    semester = models.CharField(max_length=10,
                                 choices=SEMESTER)
    note = models.FloatField(validators=[MaxValueValidator(10.0),MinValueValidator(0.0)])
    student_has_discipline_id = models.ForeignKey(Student_has_Discipline,on_delete=models.CASCADE)
    

       #aa I stopped using that form and created the relationship table manually
    #student_id = models.OneToOneField(StudentModel,null=False,on_delete=CASCADE,unique=True)
    #discipline_id = models.OneToOneField(DisciplineModel,null=False,on_delete=CASCADE,unique=True)
   
    



    
