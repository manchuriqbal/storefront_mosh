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

    with transaction.atomic():

        order = Order()
        order.customer_id = 10
        order.save()

        items = OrderItem()
        items.order = order
        items.product_id = 15
        items.quantity = 17
        items.unit_price = 85
        items.save()


    return render(request, 'hello.html', {'name': 'Mosh'})
     