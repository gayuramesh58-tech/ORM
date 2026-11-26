# Ex02 Django ORM Web Application
## Date:26/11/2026 

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).



## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Student,StudentAdmin

admin.site.register(Student,StudentAdmin)

models.py

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
```


## OUTPUT
![alt text](<Screenshot 2026-11-26 131600.png>)



## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
