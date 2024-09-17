from rest_framework import serializers
from sorl.thumbnail import get_thumbnail
from .models import ThumbnailModel

class YourModelSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = ThumbnailModel
        fields = ['id', 'image', 'thumbnail']  

    def get_thumbnail(self, obj):
        if obj.image:  
            thumbnail = get_thumbnail(obj.image, '200x200', crop='center', quality=90)
            return thumbnail.url
        return None