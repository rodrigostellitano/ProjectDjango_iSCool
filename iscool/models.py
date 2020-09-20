from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse

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
    student_id = models.AutoField(primary_key=True, verbose_name= "Matrícula")
    name = models.CharField(max_length=250,verbose_name= "Nome")
    age = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(20)],verbose_name= "Idade")
       
    def __str__(self):
        return self.name


    
        # WHY NEED TO USE ABSOLUTE URL TO CREATEVIEW?
    def get_absolute_url(self):
        return reverse('student_detail', args=[self.student_id])

    def get_absolute_url_delete(self):
        return reverse('student_delete', args=[self.student_id])

    def get_absolute_url_update(self):
        return reverse('student_edit', args=[self.pk])


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
    

     
    



    
