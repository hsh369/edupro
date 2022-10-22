from django.urls import path
from .views import *

urlpatterns = [
    path('',ClassDetail.as_view(),name='user-details'),
]
