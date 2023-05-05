from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from store.models import Product, Collection, Order, OrderItem
from tags.models import TaggedItem

def say_hello(request):

    with connection.cursor() as cursor:
        cursor.execute("SELECT title, id FROM store_product")

    # queryset = Product.objects.raw("SELECT * FROM store_product")

    return render(request, 'hello.html', {'name': 'Mosh'})
  