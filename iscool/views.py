from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from . models import StudentModel

# Create your views here.

class isCoolStudentListView(ListView):
    model = StudentModel
    template_name = 'iscool/home.html'



    # WHY NEED TO USE ABSOLUTE URL IN MODEL TO CREATEVIEW?
class isCoolStudentRegisterView(CreateView):
    model = StudentModel
    template_name = 'iscool/student_register.html'
    fields = '__all__'
    

class isCoolStudentDetailView(DetailView):
    model = StudentModel
    template_name = 'iscool/student_detail.html'
    
