from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views
from pprint import pprint

router= routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet)
router.register('carts', views.CartViewSet, basename='carts')
router.register('customers', views.CustomerViewSet, basename='customer')
router.register('orders', views.OrderViewSet)


review_router= routers.NestedDefaultRouter(router, "products", lookup="product")
review_router.register("reviews", views.ReviewViewSet, basename="product-review")

items_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
items_router.register("items", views.CartItemViewSet, basename="cart-items")

 
# URLConf no 

urlpatterns = [
    path("", include(router.urls)),
    path("", include(review_router.urls)),
    path("", include(items_router.urls)),
]

