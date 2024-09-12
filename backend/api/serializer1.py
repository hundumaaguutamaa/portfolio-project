from rest_framework import serializers
from .models import ITTeam, RequestService, UserRequest

class ITTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITTeam
        fields = ['team_id', 'team_name', 'expertise_areas']

class RequestServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestService
        fields = ['service_id', 'service_name', 'description']

class UserRequestSerializer(serializers.ModelSerializer):
    service = RequestServiceSerializer()  # Nested serializer
    team = ITTeamSerializer()  # Nested serializer

    class Meta:
        model = UserRequest
        fields = ['request_id', 'service', 'request_description', 'team', 'request_status']
