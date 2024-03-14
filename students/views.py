from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm, CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.http import HttpResponseServerError

# Create your views here.
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
            form = CreateUserForm()

    context = {'form': form}
    return render(request, 'students/register.html', context)

# from django.shortcuts import redirect

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect based on user's role
            if user.groups.filter(name='admin').exists():
                return redirect('index')
            else:
                return redirect('user-page')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'students/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def userPage(request):
    try:
        user = request.user
        student = get_object_or_404(Student, user=user)
        return render(request, 'students/user.html', {'student': student})
    except Student.DoesNotExist:
        return HttpResponseServerError("Student does not exist for the current user")

   

@login_required(login_url='login')
@admin_only
def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

@login_required(login_url='login')
def view_student(request):
    try:
        user = request.user
        student = get_object_or_404(Student, user=user)
        print("hooo")
        return render(request, 'students/user.html', {'student': student})
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {e}")   
         
@login_required(login_url='login')
def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_registration_number = form.cleaned_data['registration_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_course = form.cleaned_data['course']
      new_marks = form.cleaned_data['marks']

    new_student = Student(
        registration_number=new_registration_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        course=new_course,
        marks=new_marks
      )
    new_student.save()
    return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })

@login_required(login_url='login')
def edit(request, id):
    if request.method == 'POST':
      student = Student.objects.get(pk=id)
      form = StudentForm(request.POST, instance=student)
      if form.is_valid():
        form.save()
        return render(request, 'students/edit.html', {
          'form': form,
          'success': True
        })
    else:
      student = Student.objects.get(pk=id)
      form = StudentForm(instance=student)
      return render(request, 'students/edit.html', {
      'form': form
  })

@login_required(login_url='login')
def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))