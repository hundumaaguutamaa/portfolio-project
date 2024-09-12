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
    service = serializers.PrimaryKeyRelatedField(queryset=RequestService.objects.all())
    team = serializers.PrimaryKeyRelatedField(queryset=ITTeam.objects.all())

    class Meta:
        model = UserRequest
        fields = ['request_id', 'service', 'request_description', 'team', 'request_status']

    def create(self, validated_data):
        return UserRequest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.service = validated_data.get('service', instance.service)
        instance.request_description = validated_data.get('request_description', instance.request_description)
        instance.team = validated_data.get('team', instance.team)
        instance.request_status = validated_data.get('request_status', instance.request_status)
        instance.save()
        return instance