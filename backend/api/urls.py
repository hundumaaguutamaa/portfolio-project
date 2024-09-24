from django.urls import path, include
from .views import SignupView
from .views import SearchView
from rest_framework.routers import DefaultRouter
from .views import ITTeamViewSet, RequestServiceViewSet, UserRequestViewSet, SearchByITTeam, SearchByExpertiseArea

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('Search', SearchView, basename='Search')
router.register(r'itteams', ITTeamViewSet)
router.register(r'requestservices', RequestServiceViewSet)
router.register(r'userrequests', UserRequestViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupView.as_view(), name='signup'),
]