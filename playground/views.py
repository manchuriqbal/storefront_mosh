from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Min, Max, Avg
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Collection, Order, OrderItem, Customer
from tags.models import TaggedItem

def say_hello(request):
    discounted_price = ExpressionWrapper( F("unit_price") * 0.8, output_field=DecimalField())

    queryset = Product.objects.annotate(
        discounted_price = discounted_price
    )

    return render(request, 'hello.html', {'name': 'Mosh', "produts" : list(queryset)})
     