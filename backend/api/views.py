from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ITTeam, RequestService, UserRequest, ExpertiseArea
from .serializers import ITTeamSerializer, ExpertiseAreaSerializer, RequestServiceSerializer, UserRequestSerializer

# Search ITTeam by team_name and return associated expertise areas
class SearchByITTeam(APIView):
    def get(self, request, team_name):
        try:
            team = list(ITTeam.objects.values(team_name=team_name))
            expertise_areas = list(team.expertise_areas.values())
            serializer = ExpertiseAreaSerializer(expertise_areas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ITTeam.DoesNotExist:
            return JsonResponse({"error": "IT Team not found"}, status=status.HTTP_404_NOT_FOUND)

# Search by expertise_area and return associated teams
class SearchByExpertiseArea(APIView):
    def get(self, request, expertise_area_name):
        teams = ITTeam.objects.filter(expertise_areas__name=expertise_area_name)
        serializer = ITTeamSerializer(teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# CRUD operations for ITTeam
class ITTeamViewSet(viewsets.ModelViewSet):
    queryset = ITTeam.objects.all()
    serializer_class = ITTeamSerializer

# CRUD operations for RequestService
class RequestServiceViewSet(viewsets.ModelViewSet):
    queryset = RequestService.objects.all()
    serializer_class = RequestServiceSerializer

# CRUD operations for UserRequest
class UserRequestViewSet(viewsets.ModelViewSet):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer

class SearchView(APIView):
    def get(self, request):
        team_name = request.query_params.get('team_name', '').strip()
        expertise_area_name = request.query_params.get('expertise_area', '').strip()

        # Start with the ITTeam queryset
        queryset = ITTeam.objects.all()

        # Filter by team name if provided
        if team_name:
            queryset = queryset.filter(team_name__icontains=team_name)

        # Filter by expertise area if provided
        if expertise_area_name:
            queryset = queryset.filter(expertise_areas__name__icontains=expertise_area_name)

        # Serialize the results
        serializer = ITTeamSerializer(queryset, many=True)

        # Return the results
        return JsonResponse(serializer.data, safe=False)