from typing import Any
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models import Count

from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Product, Collection
from .serializer import ProductSerializer, CollectionSerializer

# Create your views here.

class ProductList(APIView):

    def get(self, request):
        queryset = Product.objects.select_related("collection").all()
        serializer= ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class ProductDetails(APIView):
    
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer= ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        if product.orderitems.count() > 1:
            return Response({"error" : "it can't be deleted, beacuse this is associate with OrderItem"},status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CollectionList(APIView):
    def get(self, request):
        queryset= Collection.objects.annotate(product_count=Count("products")).all()
        serializer= CollectionSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    def post(self, request):
        serializer=CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    

class CollectionDeatils(APIView):
    def get(self, request, pk):
        collection= get_object_or_404(
        Collection.objects.annotate(
        product_count=Count("products")), pk= pk)
        serializer= CollectionSerializer(collection)
        return Response(serializer.data)
    def put(self, request, pk):
        collection= get_object_or_404(
        Collection.objects.annotate(
        product_count=Count("products")), pk= pk)
        serializer=CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(Collection, status=status.HTTP_202_ACCEPTED)
    def delete(self, request, pk):
        collection= get_object_or_404(
        Collection.objects.annotate(
        product_count=Count("products")), pk= pk)
        if collection.products.count() > 0:
            return Response({"error" : "it can't be deleted, beacuse this collection have Products "},status=status.HTTP_404_NOT_FOUND)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)