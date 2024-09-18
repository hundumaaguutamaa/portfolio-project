from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ITTeamViewSet, RequestServiceViewSet, UserRequestViewSet, SearchByITTeam, SearchByExpertiseArea

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'itteams', ITTeamViewSet)
router.register(r'requestservices', RequestServiceViewSet)
router.register(r'userrequests', UserRequestViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('search/team/<str:team_name>/', SearchByITTeam.as_view(), name='search_by_team'),
    path('search/expertise/<str:expertise_area_name>/', SearchByExpertiseArea.as_view(), name='search_by_expertise'),
]
