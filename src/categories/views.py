from rest_framework import permissions, viewsets

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Category.objects.all()
