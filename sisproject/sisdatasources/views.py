from django.shortcuts import render
from rest_framework import serializers, viewsets, routers
from sisdatasources.models import Sisdatasource
from sisdatasources.serializers import SisdatasourceSerializer

# Create your views here.

# ViewSets to define the view behavior Source.


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Sisdatasource.objects.all()
    serializer_class = SisdatasourceSerializer