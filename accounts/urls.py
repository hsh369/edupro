from django.urls import path
from .views import *

urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('signup/', UserSignUpView.as_view(), name='user-create'),
    path('<int:pk>/',UserDetail.as_view(),name='user-detail'),

]
