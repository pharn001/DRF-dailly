from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from pharn.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    
    path('',include('nestedCreation.urls')),
    path('thumbnails/', include('thumnail.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)