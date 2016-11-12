from django.conf.urls import include, url
from django.contrib import admin
from sisdatasources.serializers import RegistrationSerializer
from sisdatasources.serializers import StudentSerializer
from sisdatasources.serializers import TeacherSerializer
from sisdatasources.serializers import SubjectSerializer
from sisdatasources.views import RegistrationViewSet
from sisdatasources.views import StudentViewSet
from sisdatasources.views import TeacherViewSet
from sisdatasources.views import SubjectViewSet
from rest_framework import serializers, viewsets, routers


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'registration', RegistrationViewSet)
router.register(r'student', StudentViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'subject', SubjectViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
]
