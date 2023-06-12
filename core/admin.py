from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BasedUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(BasedUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name","username","email" , "password1", "password2"),
            },
        ),
    )

class TagInline(GenericTabularInline):
    model=TaggedItem
    autocomplete_fields=['tag']

class CustomProductAdmin(ProductAdmin):
    inlines=[TagInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)