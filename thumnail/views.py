from rest_framework import viewsets
from .models import ThumbnailModel
from .serializers import YourModelSerializer

# Create your views here.
class ThumbnailModelSet(viewsets.ModelViewSet):
    queryset = ThumbnailModel.objects.all()
    serializer_class = YourModelSerializer
