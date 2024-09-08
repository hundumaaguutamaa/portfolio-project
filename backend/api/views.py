from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action  # Add this line
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from .models import ITTeam, RequestService, UserRequest
from .serializer import ITTeamSerializer, RequestServiceSerializer, UserRequestSerializer

class UserRequestFilter(FilterSet):
    q = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = UserRequest
        fields = ['q']

class ITTeamViewSet(viewsets.ModelViewSet):
    queryset = ITTeam.objects.all()
    serializer_class = ITTeamSerializer

class RequestServiceViewSet(viewsets.ModelViewSet):
    queryset = RequestService.objects.all()
    serializer_class = RequestServiceSerializer

class UserRequestViewSet(viewsets.ModelViewSet):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserRequestFilter

    # Custom action for search functionality
    @action(detail=False, methods=['get'])
    def search(self, request):
        queryset = self.get_queryset()
        filterset = self.filterset_class(request.GET, queryset=queryset)
        if filterset.is_valid():
            queryset = filterset.qs
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
