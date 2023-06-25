from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Collection, Order, OrderItem, Customer
from tags.models import TaggedItem

def say_hello(request):


    queryset = OrderItem.objects.filter(product__collection__id=3)
    
    return render(request, 'hello.html', {'name': 'Mosh', "produts" : queryset})
     