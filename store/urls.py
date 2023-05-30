from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views
from pprint import pprint

router= routers.DefaultRouter()
router.register("products", views.ProductViewSet)
router.register("collections", views.CollectionViewSet)

review_router= routers.NestedDefaultRouter(router, "products", lookup="product")
review_router.register("reviews", views.ReviewViewSet, basename="product-review")
 
# URLConf

urlpatterns = [
    path("", include(router.urls)),
    path("", include(review_router.urls))
]

