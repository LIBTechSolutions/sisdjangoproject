from django.conf.urls import include, url
from django.contrib import admin
from sisdatasources.serializers import RegistrationSerializer
from sisdatasources.serializers import StudentSerializer
from sisdatasources.views import RegistrationViewSet
from sisdatasources.views import StudentViewSet
from rest_framework import serializers, viewsets, routers


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'registration', RegistrationViewSet)
router.register(r'student', StudentViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
]
