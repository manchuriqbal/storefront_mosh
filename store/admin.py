from django.contrib import admin, messages
from typing import Any, List, Optional, Tuple
from django.db.models.query import QuerySet
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.http.request import HttpRequest
from . import models

# Register your models here.

class InventoryFilter(admin.SimpleListFilter):
    title="Inventory"
    parameter_name= "Inventory"

    def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
        return [
            ("<20", "Low")
        ]
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == "<20":
            return queryset.filter(inventory__lt=20)


@admin.register(models.Product)
class AuthorAdmin(admin.ModelAdmin):
    actions= ["clear_inventory"]
    list_display=["title", "unit_price", "inventory_stustus", "collection_title"]
    list_editable= ["unit_price"]
    list_filter = ["collection", "last_update", InventoryFilter]
    list_per_page=15
    list_select_related=["collection"]

    def collection_title(self, product):
        return product.collection.title 

    @admin.display(ordering="inventory")
    def inventory_stustus(self, Product):
        if Product.inventory < 20:
            return "Low"
        return "Ok"
    
    def clear_inventory(self,request, queryset):
        update_count=queryset.update(inventory=0)
        self.message_user(
            request,
            f"{update_count} Products ware succesfully updated",
            messages.ERROR
        )

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display= ["first_name", "last_name", "membership", "order_count"]
    list_editable=["membership"]
    list_per_page=10
    ordering= ["first_name", "last_name"]
    search_fields= ["first_name__istartswith", "last_name__istartswith"]

    @admin.display(ordering="order_count")
    def order_count(self, customer):
        url = (reverse("admin:store_order_changelist")
        + "?"
        + urlencode({
            "customer_id" : str(customer.id)
        }))
        return format_html('<a href="{}">{} </a>', url, customer.order_count)
        
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            order_count=Count("order")
        )

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display=["title", "product_count"]
    
    @admin.display(ordering="product_count")
    def product_count(self, collection):
        url=(reverse("admin:store_product_changelist")
        + "?"
        + urlencode({
           "collection_id": str(collection.id)
        }))
        return format_html('<a href="{}"> {} </a>',url, collection.product_count)
        
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            product_count=Count("product")
        )
        
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=["id", "placed_at", "customer"]

    
