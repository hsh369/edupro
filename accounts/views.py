from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveUpdateDestroyAPIView

from .serializers import UserSerializer,UserCreateSerializer,UserListSerializer
from .models import User
from rest_framework import viewsets


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'login': reverse('tutorial-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'tutorials': reverse('tutorial-list', request=request, format=format),
        'classes': reverse('tutorial-list', request=request, format=format),
    })


# Create your viewsets here.
class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    renderer_classes = [TemplateHTMLRenderer]
    #permission_classes = [IsAdminUser]

    template_name = 'user_list.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'users': queryset})



class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserSignUpView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer