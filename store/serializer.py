from decimal import Decimal
from store.models import Product, Collection, Review
from rest_framework import serializers

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Collection
        fields=["id", "title", "product_count"]
        
    product_count= serializers.IntegerField(read_only= True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= ["id", "title", "slug", "description", "unit_price", "price_with_tax", "inventory", "collection"]

    price_with_tax= serializers.SerializerMethodField(method_name="calculate_tax")
    

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields= ["id", "name", "description", "date"]

    def create(self, validated_data):
        product_id= self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)