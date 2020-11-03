from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.iscool_homepage, name="home"),
    path('underconstruction', views.isCool_under_construction,
         name="underconstruction"),

    path('student/list', views.iscool_student_list_view, name="student_list"),

    path('student/new', views.iscool_student_register_view, name="student_register"),

    path('student/details/<int:pk>',
         views.iscool_student_detail_view, name="student_detail"),

    path('student/details/<int:pk>/delete',
         views.iscool_student_delete_view, name="student_delete"),

    path('student/details/<int:pk>/edit',
         views.iscool_student_edit_view, name="student_edit"),

    path('discipline/list', views.iscool_discipline_list_view,
         name="discipline_list"),


]
