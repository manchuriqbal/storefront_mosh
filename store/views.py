from typing import Any
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models.aggregates import Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Product, Collection
from .serializer import ProductSerializer, CollectionSerializer

# Create your views here.

class ProductList(ListCreateAPIView):

    queryset= Product.objects.select_related("collection").all()
    serializer_class = ProductSerializer

    def get_serializer_context(self): 
        return {'request': self.request}


class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer

    
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitems.count() > 1:
            return Response({"error" : "it can't be deleted, beacuse this is associate with OrderItem"},status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CollectionList(ListCreateAPIView):

    queryset= Collection.objects.annotate(product_count=Count("products")).all()
    serializer_class= CollectionSerializer
    

class CollectionDeatils(RetrieveUpdateDestroyAPIView):

    queryset= Collection.objects.annotate(product_count=Count('products'))
    serializer_class= CollectionSerializer
    

    def delete(self, request, pk):
        collection= get_object_or_404(
        Collection.objects.annotate(
        product_count=Count("products")), pk= pk)
        if collection.products.count() > 0:
            return Response({"error" : "it can't be deleted, beacuse this collection have Products "},status=status.HTTP_404_NOT_FOUND)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)