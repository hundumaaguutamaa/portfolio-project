# api/urls.py
from django.urls import path
from .views import UserRequestViewSet, ITTeamViewSet, RequestServiceViewSet, UserRequestSearchView

urlpatterns = [
    path('itteam/', ITTeamViewSet.as_view({'get': 'list'})),
    path('requestservice/', RequestServiceViewSet.as_view({'get': 'list'})),
    path('userrequests/', UserRequestViewSet.as_view({'get': 'list'})),
    path('userrequests/search/', UserRequestSearchView.as_view(), name='userrequest-search'),
]
 