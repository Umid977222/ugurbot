from .models import Products
from rest_framework import serializers


class ProductSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'category', 'product', 'img', 'description', 'add_bot_button']
