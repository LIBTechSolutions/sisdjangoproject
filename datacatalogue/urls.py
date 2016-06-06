from django.conf.urls import include, url
from django.contrib import admin
from users.serializers import LDAPSerializer
from users.serializers import ContactSerializer
from users.serializers import TenantSerializer
from users.serializers import SourceSerializer
from users.views import LDAPViewSet
from users.views import ContactViewSet
from users.views import TenantViewSet
from sources.views import SourceViewSet
from rest_framework import serializers, viewsets, routers


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
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
]
