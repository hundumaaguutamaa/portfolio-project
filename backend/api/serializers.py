from rest_framework import serializers
from .models import ITTeam, ExpertiseArea, RequestService, UserRequest

# ExpertiseArea serializer
class ExpertiseAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertiseArea
        fields = ['id', 'name']

# ITTeam serializer
class ITTeamSerializer(serializers.ModelSerializer):
    # Using ExpertiseAreaSerializer to handle many-to-many relationship
    expertise_areas = ExpertiseAreaSerializer(many=True, read_only=False)
    expertise_areas_ids = serializers.PrimaryKeyRelatedField(queryset=ExpertiseArea.objects.all(), many=True, write_only=True)

    class Meta:
        model = ITTeam
        fields = ['team_id', 'team_name', 'expertise_areas', 'expertise_areas_ids']

# RequestService serializer
class RequestServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestService
        fields = ['service_id', 'service_name']

# UserRequest serializer
class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = ['request_id', 'service', 'team']
