from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from .models import ITTeam, RequestService, UserRequest
from .serializer import ITTeamSerializer, RequestServiceSerializer, UserRequestSerializer

# FilterSet for handling complex queries
class UserRequestFilter(FilterSet):
    q = CharFilter(field_name='request_description', lookup_expr='icontains')  # Search by description
    team_name = CharFilter(field_name='team__team_name', lookup_expr='icontains')  # Search by team name
    service_name = CharFilter(field_name='service__service_name', lookup_expr='icontains')  # Search by service name

    class Meta:
        model = UserRequest
        fields = ['q', 'team_name', 'service_name', 'team_id']

# ITTeam ViewSet
class ITTeamViewSet(viewsets.ModelViewSet):
    queryset = ITTeam.objects.all()
    serializer_class = ITTeamSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )

# RequestService ViewSet
class RequestServiceViewSet(viewsets.ModelViewSet):
    queryset = RequestService.objects.all()
    serializer_class = RequestServiceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )

# UserRequest ViewSet with filtering and search functionality
class UserRequestViewSet(viewsets.ModelViewSet):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserRequestFilter

    # Custom search action that can be triggered via '/userrequests/search/'
    @action(detail=False, methods=['get'])
    def search(self, request):
        queryset = self.get_queryset()
        filterset = self.filterset_class(request.GET, queryset=queryset)

        # Validate the filterset and filter results accordingly
        if filterset.is_valid():
            queryset = filterset.qs

        # Check if 'team_id' is provided in query parameters and filter by it
        team_id = request.GET.get('team_id')
        if team_id:
            queryset = queryset.filter(team__team_id=team_id)

        # Serialize and return the filtered data
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {"status": "success", "results": len(serializer.data), "data": serializer.data},
            status=status.HTTP_200_OK
        )

# Search View for User Requests with filtering and Q-based search
class UserRequestSearchView(generics.ListAPIView):
    serializer_class = UserRequestSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserRequestFilter

    def get_queryset(self):
        query = self.request.query_params.get('search', None)
        queryset = UserRequest.objects.all()

        # Use Q objects to perform complex OR-based searching
        if query:
            queryset = queryset.filter(
                Q(request_description__icontains=query) |
                Q(service__service_name__icontains=query) |
                Q(team__team_name__icontains=query)
            )
        
        # Apply additional filters (like team_name, service_name) from the filterset class
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {"status": "success", "results": len(serializer.data), "data": serializer.data},
            status=status.HTTP_200_OK
        )
