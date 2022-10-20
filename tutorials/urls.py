from django.urls import path
from .views import TutorialList

urlpatterns = [
    path('', TutorialList.as_view(), name = 'tutorial-list')
]

    