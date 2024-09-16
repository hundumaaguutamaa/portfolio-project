from rest_framework import serializers
from .models import ITTeam, RequestService, UserRequest

# ITTeam serializer to include full details
class ITTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITTeam
        fields = '__all__'
        #field = ['team_id', 'team_name', 'expertise_areas']

# RequestService serializer to include full details
class RequestServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestService
        fields = ['service_id', 'service_name', 'description']

# UserRequest serializer with nested serializers for service and team
class UserRequestSerializer(serializers.ModelSerializer):
    # Use the full serializers for service and team to include more details
    service = RequestServiceSerializer(read_only=True)
    team = ITTeamSerializer(read_only=True)

    class Meta:
        model = UserRequest
        fields = ['request_id', 'service', 'request_description', 'team']

    def create(self, validated_data):
        return UserRequest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.service = validated_data.get('service', instance.service)
        instance.request_description = validated_data.get('request_description', instance.request_description)
        instance.team = validated_data.get('team', instance.team)
        instance.request_status = validated_data.get('request_status', instance.request_status)
        instance.save()
        return instance
