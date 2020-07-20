from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(DisciplineModel)
admin.site.register(StudentModel)
admin.site.register(AvaliationModel)
admin.site.register(Student_has_Discipline  )

