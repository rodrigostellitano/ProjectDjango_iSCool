from django.urls import path

from . import views 

urlpatterns = [
    path('', views.isCoolListView.as_view() , name="home"),


]