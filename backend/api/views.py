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
            team = ITTeam.objects.get(team_name=team_name)
            expertise_areas = team.expertise_areas.all()
            serializer = ExpertiseAreaSerializer(expertise_areas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ITTeam.DoesNotExist:
            return Response({"error": "IT Team not found"}, status=status.HTTP_404_NOT_FOUND)

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
