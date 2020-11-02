from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from . models import StudentModel

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


class isCoolStudentListView(ListView):
    model = StudentModel
    template_name = 'iscool/student/student_list.html'
    context_object_name = 'student_age'

    def get_queryset(self):

        # Set the query's default value to "" if not an error, you probably look for a query with a value of NONE (error you presented) and find nothing.
        query_student_name = self.request.GET.get('query_student_name', "")
        #query_age = self.request.GET.get('query_age', "")

        object_list = StudentModel.objects.filter(
            Q(name__icontains=query_student_name)
            # | Q(age__icontains=query_age)
        )
        return object_list

    # WHY NEED TO USE ABSOLUTE URL IN MODEL TO CREATEVIEW?


class isCoolStudentRegisterView(CreateView):
    model = StudentModel
    template_name = 'iscool/student/student_register.html'
    fields = '__all__'


class isCoolStudentDetailView(DetailView):
    model = StudentModel
    template_name = 'iscool/student/student_detail.html'


class isCoolStudentDeleteView(SuccessMessageMixin, DeleteView):
    model = StudentModel
    template_name = 'iscool/student/student_delete.html'
    success_url = reverse_lazy('student_list')

    success_message = "%(name)s - Deletado com sucesso!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(isCoolStudentDeleteView, self).delete(request, *args, **kwargs)


class isCoolStudentEditView(SuccessMessageMixin, UpdateView):
    model = StudentModel
    template_name = 'iscool/student/student_edit.html'
    fields = '__all__'
    success_message = "%(name)s - alterado com sucesso!"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, fields=self.object.student_id,)


class isCoolHomePage(TemplateView):

    template_name = 'iscool/home.html'


class isCoolUnderConstruction(TemplateView):

    template_name = 'iscool/underconstruction.html'
