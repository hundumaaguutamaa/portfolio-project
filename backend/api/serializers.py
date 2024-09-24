from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
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

class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    # Validating the password confirmation
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
