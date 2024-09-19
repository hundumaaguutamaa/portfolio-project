from rest_framework import serializers
from .models import ITTeam, ExpertiseArea, RequestService, UserRequest

class ExpertiseAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertiseArea
        fields = ['id', 'name']

class ITTeamSerializer(serializers.ModelSerializer):
    expertise_areas = ExpertiseAreaSerializer(many=True)  # Nested serializer

    class Meta:
        model = ITTeam
        fields = ['team_id', 'team_name', 'expertise_areas']

    def create(self, validated_data):
        expertise_areas_data = validated_data.pop('expertise_areas', [])
        team = ITTeam.objects.create(**validated_data)
        
        # Adding ManyToMany relationships
        for expertise_data in expertise_areas_data:
            expertise_area = ExpertiseArea.objects.get(id=expertise_data['id'])
            team.expertise_areas.add(expertise_area)
        
        return team

    def update(self, instance, validated_data):
        expertise_areas_data = validated_data.pop('expertise_areas', [])
        
        # Update basic fields
        instance.team_name = validated_data.get('team_name', instance.team_name)
        instance.save()

        # Update ManyToMany relationships
        instance.expertise_areas.clear()  # Clear the current expertise areas
        for expertise_data in expertise_areas_data:
            expertise_area = ExpertiseArea.objects.get(id=expertise_data['id'])
            instance.expertise_areas.add(expertise_area)
        
        return instance

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
