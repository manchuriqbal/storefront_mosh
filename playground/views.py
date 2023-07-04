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
    
    content_type = ContentType.objects.get_for_model(Product)

    queryset = TaggedItem.objects \
    .select_related('tag') \
    .filter(
        content_type = content_type,
        object_id = 1
    )

    return render(request, 'hello.html', {'name': 'Mosh', "produts" : list(queryset)})
     