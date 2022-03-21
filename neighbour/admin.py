from django.contrib import admin
from .models import Neighbourhood, Police, HealthDepartment, Businesses, Posts, Occupants

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Police)
admin.site.register(HealthDepartment)
admin.site.register(Businesses)
admin.site.register(Posts)
admin.site.register(Occupants)
