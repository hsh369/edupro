from django.shortcuts import render

from rest_framework.viewsets import generics

from .models import Tutorial
from . serializers import TutorialSerializer

from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class TutorialList(generics.ListCreateAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tutorials': reverse('tutorial-list', request=request, format=format)
    })
