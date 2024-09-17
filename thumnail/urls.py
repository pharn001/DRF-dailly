from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ThumbnailModel
router = DefaultRouter()
router.register(r'thumbnails', ThumbnailModel)

urlpatterns = [
    path('', include(router.urls)),
]
