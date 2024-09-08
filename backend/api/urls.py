from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ITTeamViewSet, RequestServiceViewSet, UserRequestViewSet

router = DefaultRouter()
router.register(r'itteams', ITTeamViewSet)
router.register(r'requestservices', RequestServiceViewSet)
router.register(r'userrequests', UserRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
