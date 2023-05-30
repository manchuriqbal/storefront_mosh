from typing import Any
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models.aggregates import Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Product, Collection, OrderItem, Review
from .serializer import ProductSerializer, CollectionSerializer, ReviewSerializer

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self): 
        return {'request': self.request}
<<<<<<< HEAD
    
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs["pk"]).count() > 0:
=======


class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer

    
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitems.count() > 1:
>>>>>>> 0236d2dfe25fc01f566c85c85a5d3fc2a0c14da4
            return Response({"error" : "it can't be deleted, beacuse this is associate with OrderItem"},status=status.HTTP_404_NOT_FOUND)
        return super().destroy(request, *args, **kwargs)

    
class CollectionViewSet(ModelViewSet):
    queryset= Collection.objects.annotate(product_count=Count("products")).all()
    serializer_class= CollectionSerializer

<<<<<<< HEAD
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs["pk"]).count() > 0:
=======
class CollectionDeatils(RetrieveUpdateDestroyAPIView):

    queryset= Collection.objects.annotate(product_count=Count('products'))
    serializer_class= CollectionSerializer
    

    def delete(self, request, pk):
        collection= get_object_or_404(
        Collection.objects.annotate(
        product_count=Count("products")), pk= pk)
        if collection.products.count() > 0:
>>>>>>> 0236d2dfe25fc01f566c85c85a5d3fc2a0c14da4
            return Response({"error" : "it can't be deleted, beacuse this collection have Products "},status=status.HTTP_404_NOT_FOUND)
        return super().destroy(request, *args, **kwargs)
    
class ReviewViewSet(ModelViewSet):

    serializer_class= ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs["product_pk"])
    
    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}
