from django.urls import path,include
from .views import *

from rest_framework import routers

from .views import ClassViewSet

router = routers.SimpleRouter()
router.register(r'classes',ClassViewSet)


urlpatterns = [
    path('',include((router.urls, 'classes'))),
]
