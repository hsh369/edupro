"""edupro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import urls
#custom admin site
from django.contrib import admin
admin.site.site_header = 'edupro admin'
admin.site.site_title = 'edupro'
admin.site.index_title = 'EDUPRO administration'
admin.empty_value_display = '**Empty**'
#deloyed url
#admin.site.site_url = 'http://edupro.com/'


from accounts.views import api_root

from rest_framework import routers

from classes.views import ClassViewSet

router = routers.SimpleRouter()
router.register(r'classes',ClassViewSet)

urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('tutorials/',include('tutorials.urls')),
    path('',include((router.urls, 'classes'))),
    path('accounts/',include('accounts.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]
