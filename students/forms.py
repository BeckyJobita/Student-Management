from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields =  ['registration_number', 'first_name', 'last_name', 'email', 'course', 'marks']
        labels = {
      'registration_number': 'Registration Number',
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'email': 'Email',
      'course': 'Course',
      'marks': 'Marks'
    }

    widgets = {
      'registration_number': forms.NumberInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'course': forms.TextInput(attrs={'class': 'form-control'}),
      'marks': forms.NumberInput(attrs={'class': 'form-control'}),
    }

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']