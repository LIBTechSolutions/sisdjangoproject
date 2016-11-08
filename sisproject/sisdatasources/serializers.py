from django.shortcuts import render
from django.conf.urls import include, url
from django.contrib import admin
from .models import Registration
from .models import Student
from rest_framework import serializers, viewsets, routers


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Registration
        fields = ('lastName', 'middleName',
                  'firstName', 'gender', 'phone_number', 'email',
                  'address', 'city', 'county', 'nationality',
                  'dateOfBirth', 'placeOfBirth', 'country',
                  'emergency', 'emergency_phone', 'previous_school',
                  'transcript')


class StudentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = ('registration', 'level', 'grade', 'student_photo')
