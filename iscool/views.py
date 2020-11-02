from django.shortcuts import render, redirect

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from . models import StudentModel, DisciplineModel
from . forms import StudentForm


# Create your views here.


class isCoolStudentListView(ListView):
    model = StudentModel
    template_name = 'iscool/student/student_list.html'
    context_object_name = 'student_age'

    def get_queryset(self):

        # Set the query's default value to "" if not an error, you probably look for a query with a value of NONE (error you presented) and find nothing.
        query_student_name = self.request.GET.get('query_student_name', "")
        # query_age = self.request.GET.get('query_age', "")

        object_list = StudentModel.objects.filter(
            Q(name__icontains=query_student_name)
            # | Q(age__icontains=query_age)
        )
        return object_list


def iscool_student_register_view(request):

    template_name = 'iscool/student/student_register.html'
    form = StudentForm(request.POST or None)
    context = {}

    if form.is_valid():
        detail_id = form.save()

        return redirect('student_detail', detail_id.pk)

    context = {"form": form}

    return render(request, template_name, context)


def iscool_student_detail_view(request, pk):
    template_name = 'iscool/student/student_detail.html'
    context = {}
    try:
        context["StudentModel"] = StudentModel.objects.get(pk=pk)
    except StudentModel.DoesNotExist:
        raise Http404
    return render(request, template_name, context)


class isCoolStudentDeleteView(SuccessMessageMixin, DeleteView):
    model = StudentModel
    template_name = 'iscool/student/student_delete.html'
    success_url = reverse_lazy('student_list')

    success_message = "%(name)s - Deletado com sucesso!"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(isCoolStudentDeleteView, self).delete(request, *args, **kwargs)


class isCoolStudentEditView(SuccessMessageMixin, UpdateView):
    model = StudentModel
    template_name = 'iscool/student/student_edit.html'
    fields = '__all__'
    success_message = "%(name)s - alterado com sucesso!"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, fields=self.object.student_id,)


def iscool_student_edit_view(request, pk):
    context = {}
    student = StudentModel.objects.get(pk=pk)

    form = StudentForm(request.POST or None, instance=student)
    context['student'] = student
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            edit_id = form.save()
            print(edit_id.pk)
            messages.success(
                request, f'O estudante: {student.name} foi alterado com sucesso!')
            return redirect('student_detail', edit_id.pk)
            # , edit_id.pk)
    else:
        return render(request, "iscool/student/student_edit.html", context)


def iscool_homepage(request):
    template_name = 'iscool/home.html'
    return render(request, template_name)


def isCool_under_construction(request):
    template_name = 'iscool/underconstruction.html'
    return render(request, template_name)


def iscool_discipline_list_view(request):
    try:
        obj = DisciplineModel.objects.all()

    except DisciplineModel.DoesNotExist:
        raise Http404
    return render(request, 'iscool/discipline/discipline_list.html',
                  {'obj': obj})

  # WHY NEED TO USE ABSOLUTE URL IN MODEL TO CREATEVIEW?
# class isCoolStudentRegisterView(CreateView):
#     model = StudentModel
#     template_name = 'iscool/student/student_register.html'
#     fields = '__all__'


# class isCoolStudentDetailView(DetailView):
#     model = StudentModel
#     template_name = 'iscool/student/student_detail.html'


# class isCoolHomePage(TemplateView):

#     template_name = 'iscool/home.html'


# class isCoolUnderConstruction(TemplateView):

#     template_name = 'iscool/underconstruction.html'
