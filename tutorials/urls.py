from django.urls import path,include
from .views import TutorialCreate, TutorialDelete, TutorialList,TutorialDetail, TutorialUpdate
from rest_framework import routers
from .views import BlogViewSet

router = routers.SimpleRouter()
router.register(r'blogs',BlogViewSet)


urlpatterns = [ 
    path('', TutorialList.as_view(), name = 'tutorial-list'),
    path('create/', TutorialCreate.as_view(), name = 'tutorial-create'),
    path('detail/<int:pk>',TutorialDetail.as_view(), name = 'tutorial-detail-view'),
    path('update/<int:pk>',TutorialUpdate.as_view(), name = 'tutorial-update'),
    path('delete/<int:pk>',TutorialDelete.as_view(), name = 'tutorial-delate'),
    path('<int:pk>/',include((router.urls, 'blogs')))
]

# urlpatterns += router.urls
    