from django.urls import path 
from .views import CheckPermissionView
urlpatterns = [
    path('data/',CheckPermissionView.as_view(),name='check-permission'),
]