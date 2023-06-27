from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Collection, Order, OrderItem, Customer
from tags.models import TaggedItem

def say_hello(request):

    queryset = Order.objects.select_related("customer").prefetch_related("items__product").order_by("-placed_at")[:5]

    return render(request, 'hello.html', {'name': 'Mosh', "produts" : list(queryset)})
     