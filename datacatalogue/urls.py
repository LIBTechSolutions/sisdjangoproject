"""datacatalogue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
# from django.contrib.auth.models import LDAP
from users.models import LDAP
from users.models import Contact
from users.models import Tenant
from sources.models import Source
from rest_framework import serializers, viewsets, routers

# Serializers define the API representation.


class LDAPSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = LDAP
        fields = ('dc', 'cn', 'ou', 'o', 'street', 'l', 'street', 'cn', 'uid', 'dn')


# ViewSets to define the view behavior LDAP.
class LDAPViewSet(viewsets.ModelViewSet):
    queryset = LDAP.objects.all()
    serializer_class = LDAPSerializer


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email_address', 'phone_number', 'ldap_id')


# ViewSets to define the view behavior Contact.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class TenantSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Tenant
        fields = ('role', 'contact_id', 'url')


# ViewSets to define the view behavior Tenant.
class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Source
        fields = ('tenant_id', 'contact_id', 'access_method', 'availability', 
                  'compression', 'description', 'digital_rights', 'encoding',
                  'encryption', 'encryption', 'language', 'last_accessed', 
                  'last_modified', 'last_refreshed', 'license_type', 
                  'maintainer', 'maintainer_email', 'maintainer_phone', 'pii',
                  'records', 'regex', 'schema_type', 'size', 'system_of_record',
                  'uri_access', 'uri_documenation', 'uri_endpoint', 'uri_schema', 
                  'title', 'visibility')


# ViewSets to define the view behavior Source.
class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'ldap', LDAPViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'tenant', TenantViewSet)
router.register(r'source', SourceViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('pages.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
