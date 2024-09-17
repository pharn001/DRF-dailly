from django.db import models
class ThumbnailModel(models.Model):
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f"Image ID: {self.id}"  

    class Meta:
        verbose_name = "Thumbnail"
        verbose_name_plural = "Thumbnails"
