from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ThumbnailModelSet

router = DefaultRouter()
router.register(r'Thumbnails', ThumbnailModelSet)
urlpatterns = [
    path('', include(router.urls)),
]
