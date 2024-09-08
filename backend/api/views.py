from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ITTeam, RequestService, UserRequest
from .serializer import ITTeamSerializer, RequestServiceSerializer, UserRequestSerializer

