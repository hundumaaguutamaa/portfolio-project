from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views  # Update with your app's views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
path('api/search/', views.SearchView.as_view()),
router.register(r'teams', views.ITTeamViewSet)
router.register(r'services', views.RequestServiceViewSet)
router.register(r'userrequests', views.UserRequestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', admin.site.urls),
    path('api/search/', views.SearchView.as_view()),
    path('api/signup/', views.SignupView.as_view()),
    #path('api/', include(router.urls)),  # Add your API routes
    path('', include(router.urls)),  # Redirect root to API

     # JWT login and refresh token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

