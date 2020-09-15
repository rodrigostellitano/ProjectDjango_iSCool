from django.urls import path

from . import views 

urlpatterns = [
    path('', views.isCoolStudentListView.as_view() , name="home"),
    path('student/new/', views.isCoolStudentRegisterView.as_view() , name="student_register"),
    path('student/details/<int:pk>', views.isCoolStudentDetailView.as_view() , name="student_detail"),
    path('student/details/<int:pk>/delete', views.isCoolStudentDeleteView.as_view() , name="student_delete"),
    path('student/details/<int:pk>/edit', views.isCoolStudentEditView.as_view() , name="student_edit"),
    

]