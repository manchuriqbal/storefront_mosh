from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Collection
from .serializer import ProductSerializer, CollectionSerializer

# Create your views here.

@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":

        queryset = Product.objects.select_related("collection").all()
        serializer= ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
@api_view(["GET", "PUT", "DELETE"])
def product_details(request, id ):  
    product = get_object_or_404(Product, pk=id)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer= ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        if product.orderitems.count() > 1:
            return Response({"error" : "it can't be deleted, beacuse this is associate with OrderItem"},status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def collection_list(request):
    if request.method == "GET":
        queryset= Collection.objects.annotate(product_count=Count("Products")).all()
        serializer= CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer=CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(["GET", "PUT", "DELETE"])
def collection_deatil(request, pk):
    collection= get_object_or_404(
        Collection.objects.annotate(
        product_count=Count("Products")), pk= pk)
    if request.method == "GET":
        serializer= CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer=CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(Collection, status=status.HTTP_202_ACCEPTED)
    elif request.method == "DELETE":
        if collection.products.count() > 0:
            return Response({"error" : "it can't be deleted, beacuse this collection have Products"},status=status.HTTP_404_NOT_FOUND)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)