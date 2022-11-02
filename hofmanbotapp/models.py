from django.db import models

# Create your models here.


def upload(instance, filename):
    return filename


class Products(models.Model):
    category = models.CharField(max_length=200, unique=True)
    product = models.CharField(max_length=200, unique=True)
    img = models.ImageField(upload_to=upload, default='posts/default.jpg')
    description = models.TextField()
    add_bot_button = models.BooleanField()
