from django.urls import path
from django.urls.conf import include
from rest_framework.routers import SimpleRouter
from . import views
from pprint import pprint

routers= SimpleRouter()
routers.register("product", views.ProductViewSet)
routers.register("collection", views.CollectionViewSet)
pprint(routers.urls)

# URLConf

urlpatterns = [
    path("", include(routers.urls))
]