from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

# Create your views here.

@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer= ProductSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def product_details(request, id ):
        
        product = get_list_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)