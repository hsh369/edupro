from django.shortcuts import render

from rest_framework.viewsets import generics
from rest_framework import viewsets

from .models import Tutorial
from .serializers import *

from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

# Create your views here.     

# TutorialCrud operations
class TutorialList(generics.ListAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialListSerializer
    #permission_classes = [permissions.IsAuthenticated]

class TutorialCreate(generics.CreateAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialDetailCreateSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly] 
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class TutorialDetail(generics.RetrieveAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialDetailCreateSerializer
    #permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly] 

    

class TutorialUpdate(generics.UpdateAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialDetailCreateSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly] 

class TutorialDelete(generics.DestroyAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialDetailCreateSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly] 


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        tutorial = self.kwargs['pk']
        return Blog.objects.filter(tutorial_id=tutorial)

