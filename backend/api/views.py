from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import ITTeam, RequestService, UserRequest
from .serializer import ITTeamSerializer, RequestServiceSerializer, UserRequestSerializer

class ITTeamViewSet(viewsets.ModelViewSet):
    queryset = ITTeam.objects.all()
    serializer_class = ITTeamSerializer

class RequestServiceViewSet(viewsets.ModelViewSet):
    queryset = RequestService.objects.all()
    serializer_class = RequestServiceSerializer

class UserRequestViewSet(viewsets.ModelViewSet):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer

    @action(detail=True, methods=['get'])
    def custom_action(self, request, pk=None):
        """
        A custom action example for UserRequest.
        This is optional and can be used for custom behavior.
        """
        user_request = self.get_object()
        serializer = self.get_serializer(user_request)
        return Response(serializer.data)
