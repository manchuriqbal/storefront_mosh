from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

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

@api_view()
def collection_deatil(request, pk):
    return Response("Ok")