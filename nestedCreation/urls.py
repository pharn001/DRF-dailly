from django.urls import path
from .views import OrderCreateView

urlpatterns = [
    path('create-order/',OrderCreateView.as_view(),name='create-order'),
]