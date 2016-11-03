from django.conf.urls import include, url
from django.contrib import admin
from sisdatasources.serializers import SisdatasourceSerializer
from sisdatasources.views import SourceViewSet
from rest_framework import serializers, viewsets, routers


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'sisdatasource', SourceViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
]
