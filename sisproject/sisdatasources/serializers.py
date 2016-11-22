# from django.shortcuts import render
# from django.conf.urls import include, url
# from django.contrib import admin
# from .models import Registration
# from .models import Student
# from .models import Teacher
# from .models import Subject
# from rest_framework import serializers, viewsets, routers


# class RegistrationSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Registration
#         fields = ('lastName', 'middleName',
#                   'firstName', 'gender', 'phone_number', 'email',
#                   'address', 'city', 'county', 'nationality',
#                   'dateOfBirth', 'placeOfBirth', 'country',
#                   'emergency', 'emergency_phone', 'previous_school',
#                   'transcript')


# class StudentSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Student
#         fields = ('registration', 'level', 'grade', 'student_photo')


# class TeacherSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Teacher
#         fields = ('teacherID', 'lastName', 'middleName', 'firstName',
#                   'gender', 'phone_number', 'email', 'dateOfBirth',
#                   'placeOfBirth', 'nationality', 'qualification',
#                   'experience', 'licence', 'teacher_photo', 'age',
#                   'created', 'modified')


# class SubjectSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Subject
#         fields = ('teacher_ID', 'subject', 'schedule', 'teacher')
