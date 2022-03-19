from django.contrib import admin
from .models import Neighbourhood, Police, HealthDepartment

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Police)
admin.site.register(HealthDepartment)
