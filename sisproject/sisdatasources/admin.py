from django.contrib import admin

# Register your models here.
from .models import Registration
from .models import Student
from .models import Teacher
from .models import Subject


class RegistrationModelAdmin(admin.ModelAdmin):
    list_display = ["lastName", "middleName", "firstName", "gender",
                    "phone_number", "email", "address", "city",
                    "county", "nationality", "dateOfBirth",
                    "placeOfBirth", "country", "emergency", "emergency_phone",
                    "previous_school", "transcript", "created", "modified"]
    list_display_links = ["lastName"]
    list_filter = ["lastName", "middleName", "firstName"]
    list_editable = ["firstName"]
    search_fields = ["lastName", "firstName"]

    class Meta:
        model = Registration

admin.site.register(Registration, RegistrationModelAdmin)


class StudentModelAdmin(admin.ModelAdmin):
    list_display = ["registration", "level", "grade", "student_photo"]
    list_display_links = ["registration"]
    list_filter = ["level", "grade"]
    search_fields = ["level", "grade"]

    class Meta:
        model = Student

admin.site.register(Student, StudentModelAdmin)


class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ["teacherID", "lastName", "middleName", "firstName",
                    "gender", "phone_number", "email", "dateOfBirth",
                    "placeOfBirth", "nationality", "qualification",
                    "experience", "licence", "teacher_photo", "age",
                    "created", "modified"]
    list_display_links = ["teacherID"]
    list_filter = ["lastName", "middleName", "firstName"]
    list_editable = ["firstName"]
    search_fields = ["lastName", "firstName"]

    class Meta:
        model = Teacher

admin.site.register(Teacher, TeacherModelAdmin)


class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ["teacher_ID", "subject", "schedule", "teacher"]
    list_display_links = ["subject"]
    list_filter = ["subject", "schedule"]
    search_fields = ["subject", "schedule"]

    class Meta:
        model = Subject

admin.site.register(Subject, SubjectModelAdmin)
