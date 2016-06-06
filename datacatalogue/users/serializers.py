from django.shortcuts import render
from django.conf.urls import include, url
from django.contrib import admin
from sources.models import Source
from users.models import LDAP
from users.models import Contact
from users.models import Tenant
from rest_framework import serializers, viewsets, routers


class LDAPSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = LDAP
        fields = ('dc', 'cn', 'ou', 'o', 'street', 'l', 'street', 'cn', 'uid', 
        	      'dn')


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email_address', 'phone_number', 
        	      'ldap_id')


class TenantSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Tenant
        fields = ('role', 'contact_id', 'url')


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Source
        fields = ('tenant_id', 'contact_id', 'access_method', 'availability', 
                  'compression', 'description', 'digital_rights', 'encoding',
                  'encryption', 'encryption', 'language', 'last_accessed', 
                  'last_modified', 'last_refreshed', 'license_type', 
                  'maintainer', 'pii', 'records', 'regex',
                  'schema_type', 'size', 'system_of_record', 'uri_access', 
                  'uri_documenation', 'uri_endpoint', 'uri_schema', 
                  'title', 'visibility')

