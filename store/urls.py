from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetails.as_view()),
    path('collection/', views.CollectionList.as_view()),
    path('collection/<int:pk>/', views.CollectionDeatils.as_view(), name="collection_deatil")
]