from django.shortcuts import render
from django.views.generic import ListView
from . models import StudentModel

# Create your views here.

class isCoolListView(ListView):
    model = StudentModel
    template_name = 'iscool/home.html'