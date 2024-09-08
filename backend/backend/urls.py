from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ITTeamViewSet, RequestServiceViewSet, UserRequestViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'itteams', ITTeamViewSet)
router.register(r'requestservices', RequestServiceViewSet)
router.register(r'userrequests', UserRequestViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
