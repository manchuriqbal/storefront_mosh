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
<<<<<<< HEAD
    path("", include(router.urls)),
    path("", include(review_router.urls))
=======
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetails.as_view()),
    path('collection/', views.CollectionList.as_view()),
    path('collection/<int:pk>/', views.CollectionDeatils.as_view(), name="collection_deatil")
>>>>>>> 0236d2dfe25fc01f566c85c85a5d3fc2a0c14da4
]