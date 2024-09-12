from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ITTeamViewSet, RequestServiceViewSet, UserRequestViewSet

# Class-Based View (CBV) approach, specifically using DRF's ViewSets and Routers for building RESTful APIs.
router = DefaultRouter()
router.register(r'itteams', ITTeamViewSet)
router.register(r'requestservices', RequestServiceViewSet)
router.register(r'userrequests', UserRequestViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # base path for your API is set
]

