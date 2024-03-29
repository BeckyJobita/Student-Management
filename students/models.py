from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    course = models.CharField(max_length=50)
    marks = models.FloatField()

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
