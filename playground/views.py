from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Collection, Order, OrderItem
from tags.models import TaggedItem

def say_hello(request):

    queryset = Product.objects.filter(unit_price__gt=20)
    
    
    

    return render(request, 'hello.html', {'name': 'Mosh', "produts" : queryset})
  