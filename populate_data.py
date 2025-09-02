from students.models import Student, Course, Enrollment
from django.contrib.auth.models import User
from datetime import date

# Courses
courses = []
courses.append(Course.objects.get_or_create(code='CSE101', defaults={'name':'Computer Science Basics','instructor':'Dr. Smith'})[0])
courses.append(Course.objects.get_or_create(code='MAT101', defaults={'name':'Mathematics I','instructor':'Prof. Johnson'})[0])
courses.append(Course.objects.get_or_create(code='PHY101', defaults={'name':'Physics I','instructor':'Dr. Brown'})[0])
courses.append(Course.objects.get_or_create(code='ENG101', defaults={'name':'English Communication','instructor':'Prof. White'})[0])

# Students
students = []
students.append(Student.objects.get_or_create(
    user=User.objects.get_or_create(username='john123', defaults={'email':'john@example.com','first_name':'John','last_name':'Doe'})[0],
    defaults={'student_id':'STU001','date_of_birth':date(2000,5,14)}
)[0])

students.append(Student.objects.get_or_create(
    user=User.objects.get_or_create(username='sara456', defaults={'email':'sara@example.com','first_name':'Sara','last_name':'Smith'})[0],
    defaults={'student_id':'STU002','date_of_birth':date(2001,8,22)}
)[0])

students.append(Student.objects.get_or_create(
    user=User.objects.get_or_create(username='alex789', defaults={'email':'alex@example.com','first_name':'Alex','last_name':'Brown'})[0],
    defaults={'student_id':'STU003','date_of_birth':date(2002,2,10)}
)[0])

students.append(Student.objects.get_or_create(
    user=User.objects.get_or_create(username='emma321', defaults={'email':'emma@example.com','first_name':'Emma','last_name':'White'})[0],
    defaults={'student_id':'STU004','date_of_birth':date(2000,12,5)}
)[0])

# Enrollments
Enrollment.objects.get_or_create(student=students[0], course=courses[0])
Enrollment.objects.get_or_create(student=students[0], course=courses[1])
Enrollment.objects.get_or_create(student=students[1], course=courses[1])
Enrollment.objects.get_or_create(student=students[1], course=courses[2])
Enrollment.objects.get_or_create(student=students[2], course=courses[0])
Enrollment.objects.get_or_create(student=students[2], course=courses[3])
Enrollment.objects.get_or_create(student=students[3], course=courses[2])
Enrollment.objects.get_or_create(student=students[3], course=courses[3])

print("✅ Courses, students, and enrollments created successfully!")
