from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, StudentProfileForm
from .models import Student, Course, Enrollment

# Welcome page
def welcome(request):
    return render(request, 'welcome.html')

# User registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            
            # Authenticate and login the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Account created successfully! Welcome {username}!')
                return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegisterForm()
    
    return render(request, 'students/register.html', {'form': form})

# Student dashboard
@login_required
def dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
        enrollments = Enrollment.objects.filter(student=student)
        courses = [enrollment.course for enrollment in enrollments]
    except Student.DoesNotExist:
        messages.warning(request, 'You need to complete registration first.')
        return redirect('register')
    
    context = {
        'student': student,
        'courses': courses,
        'enrollments': enrollments,
    }
    return render(request, 'students/dashboard.html', context)

# Student profile view & update
@login_required
def profile(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        messages.error(request, 'Student profile not found. Please complete registration.')
        return redirect('register')
    
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentProfileForm(instance=student)
    
    return render(request, 'students/profile.html', {'form': form, 'student': student})


    # View to show all students
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
