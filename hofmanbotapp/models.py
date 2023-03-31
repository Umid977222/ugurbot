from django.db import models

# Create your models here.


def upload(instance, filename):
    return '/'.join(['products', str(instance.id), filename])


class Products(models.Model):
    VALUE_TYPE2 = (
        ('1', 'CAN COOLERS'),
        ('2', 'CABINETS'),
        ('3', 'CHEST FREEZERS'),
        ('4', 'CHEST COOLERS'),
        ('5', 'CONDITIONERS'),
        ('6', 'CONSERVATORS'),
        ('7', 'COUNTER COOLERS'),
        ('8', 'DOOR COOLERS'),
        ('9', 'DISPENSERS'),
        ('10', 'ENERGY EFFICIENT'),
        ('11', 'FRONT COOLERS'),
        ('12', 'ICE SHOW'),
        ('13', 'ICE MACHINES'),
        ('14', 'MICRO'),
        ('15', 'PREMIUM COOLERS'),
        ('16', 'UPRIGHT FREEZERS'),
        ('17', 'SUB-ZERO'),
        ('18', 'SUPERMARKET FREEZERS'),
        ('19', 'SUPERMARKET COOLERS'),
        ('20', 'POOL TYPE'),
        ('21', 'WATER'))
    category = models.CharField(max_length=200, choices=VALUE_TYPE2)
    product = models.CharField(max_length=200, unique=True)
    img = models.ImageField(upload_to=upload, default='posts/default.jpg')
    description = models.TextField()
    add_bot_button = models.BooleanField()
