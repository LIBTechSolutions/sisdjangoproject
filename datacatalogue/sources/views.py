from django.shortcuts import render
from rest_framework import serializers, viewsets, routers
from sources.models import Source
from users.serializers import SourceSerializer

# Create your views here.

# ViewSets to define the view behavior Source.


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer