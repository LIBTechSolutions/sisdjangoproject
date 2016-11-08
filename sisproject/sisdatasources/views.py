from django.shortcuts import render
from rest_framework import serializers, viewsets, routers
from .models import Registration
from .models import Student
from .serializers import RegistrationSerializer
from .serializers import StudentSerializer

# Create your views here.

# ViewSets to define the view behavior Source.


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
