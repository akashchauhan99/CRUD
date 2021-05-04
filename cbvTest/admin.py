from .models import Student
from django.contrib import admin

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')

admin.site.register(Student, StudentAdmin)
