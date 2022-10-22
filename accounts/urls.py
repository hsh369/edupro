from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', UserList.as_view(), name='user-list'),
    path('profile/<int:pk>/',UserDetail.as_view(),name='user-detail'),
]
