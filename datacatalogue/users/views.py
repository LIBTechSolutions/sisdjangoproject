from django.shortcuts import render
from rest_framework import serializers, viewsets, routers
from users.models import LDAP
from users.models import Contact
from users.models import Tenant
from users.serializers import LDAPSerializer
from users.serializers import ContactSerializer
from users.serializers import TenantSerializer


class LDAPViewSet(viewsets.ModelViewSet):
    queryset = LDAP.objects.all()
    serializer_class = LDAPSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer 


class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer 
