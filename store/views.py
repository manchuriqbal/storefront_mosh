from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Collection, OrderItem, Review
from .serializer import ProductSerializer, CollectionSerializer, ReviewSerializer
from .filters import ProductFilter

# Create your views here.
class ProductViewSet(ModelViewSet):
    
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class= ProductFilter
    search_fields= ["title", "description"]
 
    def get_serializer_context(self): 
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs["pk"]).count() > 0:
            return Response({"error" : "it can't be deleted, beacuse this is associate with OrderItem"},status=status.HTTP_404_NOT_FOUND)
        return super().destroy(request, *args, **kwargs)

    
class CollectionViewSet(ModelViewSet):
    queryset= Collection.objects.annotate(product_count=Count("products")).all()
    serializer_class= CollectionSerializer

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs["pk"]).count() > 0:
            return Response({"error" : "it can't be deleted, beacuse this collection have Products "},status=status.HTTP_404_NOT_FOUND)
        return super().destroy(request, *args, **kwargs)
    
class ReviewViewSet(ModelViewSet):

    serializer_class= ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs["product_pk"])
    
    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}
    
    
