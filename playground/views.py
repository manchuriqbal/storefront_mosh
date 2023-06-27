from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from django.db.models import Q, F
from django.db.models.aggregates import Count, Min, Max, Avg
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Collection, Order, OrderItem, Customer
from tags.models import TaggedItem

def say_hello(request):

    queryset = Product.objects.filter(collection_id=3).aggregate(Minimum= Min("unit_price"), Maximum= Max("unit_price"),Avgarage= Avg("unit_price"),)

    return render(request, 'hello.html', {'name': 'Mosh', "produts" : queryset})
     