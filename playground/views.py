from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Collection, Order, OrderItem, Customer
from tags.models import TaggedItem

def say_hello(request):

    queryset = Product.objects.defer("unit_price")

    return render(request, 'hello.html', {'name': 'Mosh', "produts" : list(queryset)})
     