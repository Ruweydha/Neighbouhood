from django.contrib import admin
from .models import Neighbourhood, Police, HealthDepartment, Businesses

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Police)
admin.site.register(HealthDepartment)
admin.site.register(Businesses)
