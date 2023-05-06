from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Product)
class AuthorAdmin(admin.ModelAdmin):
    list_display=["title", "unit_price", "inventory_stustus", "collection_title"]
    list_editable= ["unit_price"]
    list_per_page=15
    list_select_related=["collection"]

    def collection_title(self, product):
        return product.collection.title 

    @admin.display(ordering="inventory")
    def inventory_stustus(self, Product):
        if Product.inventory < 20:
            return "Low"
        return "Ok"


    

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display= ["first_name", "last_name", "membership"]
    list_editable=["membership"]
    list_per_page=10
    ordering= ["first_name", "last_name"]

admin.site.register(models.Collection)

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=["id", "placed_at", "customer"]

    
