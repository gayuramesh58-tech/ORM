from django.db import models
from django.contrib import admin
class Student(models.Model):
    id = models.CharField(max_length=20,primary_key=True,help_text="student ID")
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    age = models.IntegerField()
    department = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=50)

class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','roll_no','age','department','email','city')