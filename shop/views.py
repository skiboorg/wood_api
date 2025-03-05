from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from rest_framework import generics
from .models import *

# class GetInstructions(APIView):
#     def get(self, request):
#         return Response("Hello World")


class GetCategories(generics.ListAPIView):
    serializer_class = CategoryShortSerializer
    queryset = Category.objects.all()

class GetMaterials(generics.ListAPIView):
    serializer_class = MaterialShortSerializer
    queryset = Material.objects.all()

class GetCategory(generics.RetrieveAPIView):
    serializer_class = CategoryShortSerializer
    queryset = Category.objects.filter()
    lookup_field = 'slug'

class GetSubCategory(generics.RetrieveAPIView):
    serializer_class = SubCategoryShortSerializer
    queryset = SubCategory.objects.filter()
    lookup_field = 'slug'

class GetProduct(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()
    lookup_field = 'slug'


class GetServices(generics.ListAPIView):
    serializer_class = ServiceShortSerializer
    queryset = Service.objects.all()

class GetService(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.filter()
    lookup_field = 'slug'


class GetMaterial(generics.RetrieveAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.filter()
    lookup_field = 'slug'

class GetPopularProducts(generics.ListAPIView):
    serializer_class = ProductShortSerializer
    queryset = Product.objects.filter(is_active=True)

class SearchProducts(generics.ListAPIView):
    serializer_class = ProductShortSerializer
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(is_active=True, name__icontains=query)
        else:
            return Product.objects.none()