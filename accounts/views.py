from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveUpdateDestroyAPIView

from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets

# Create your viewsets here.

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAdminUser]



class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
