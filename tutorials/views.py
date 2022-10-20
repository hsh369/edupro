from django.shortcuts import render

from rest_framework.viewsets import generics

from .models import Tutorial
from . serializers import TutorialSerializer


# Create your views here.
class TutorialList(generics.ListCreateAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer