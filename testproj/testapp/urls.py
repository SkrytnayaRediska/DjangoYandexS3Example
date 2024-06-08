from django.urls import path, include
from rest_framework.routers import DefaultRouter
from testapp.views import TestViewSet


router = DefaultRouter()
router.register(r'tests', TestViewSet, basename='test')


urlpatterns = [
    path('', include(router.urls)),
]
