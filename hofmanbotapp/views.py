from rest_framework import viewsets, permissions
from .models import Products
from .serializers import ProductSerializers


# Create your views here.


class ProblemViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Products.objects.all().order_by('product')
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
