from django.db import models
import os

def upload_to_static(instance, filename):
    return os.path.join('homepage', 'static', filename)

class apartment(models.Model):
    duration = models.CharField(max_length=50, verbose_name="Length of stay")
    image1 = models.ImageField(upload_to=upload_to_static, verbose_name="Image of Room")
    image2 = models.ImageField(upload_to=upload_to_static, verbose_name="Image of Room")
    video_file = models.FileField(upload_to=upload_to_static, null=True)




