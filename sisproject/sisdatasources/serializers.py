from django.shortcuts import render
from django.conf.urls import include, url
from django.contrib import admin
from sisdatasources.models import Sisdatasource
from rest_framework import serializers, viewsets, routers


class SisdatasourceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sisdatasource
        fields = ('access_method', 'availability',
                  'compression', 'description', 'digital_rights', 'encoding',
                  'encryption', 'encryption', 'language', 'last_accessed',
                  'last_modified', 'last_refreshed', 'license_type',
                  'pii', 'records', 'json_schema',
                  'schema_type', 'size', 'system_of_record', 'uri_access',
                  'uri_documenation', 'uri_endpoint', 'uri_schema',
                  'title', 'visibility')
