from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Product)
class AuthorAdmin(admin.ModelAdmin):
    list_display=["title", "unit_price", "inventory_stustus"]
    list_editable= ["unit_price"]
    list_per_page=15

    @admin.display(ordering="inventory")
    def inventory_stustus(self, Product):
        if Product.inventory < 10:
            return "Low"
        return "Ok"


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display= ["first_name", "last_name", "membership"]
    list_editable=["membership"]
    list_per_page=10
    ordering= ["first_name", "last_name"]

admin.site.register(models.Collection)
