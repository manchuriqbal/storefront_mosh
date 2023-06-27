from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from django.db.models import Q, F, Value, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Min, Max, Avg
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Collection, Order, OrderItem, Customer
from tags.models import TaggedItem

def say_hello(request):

    queryset = Customer.objects.select_related("user").annotate(full_name=Concat("user__first_name", Value(" "), "user__last_name"))

    return render(request, 'hello.html', {'name': 'Mosh', "produts" : queryset})
     