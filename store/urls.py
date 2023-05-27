from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('product/', views.ProductList.as_view()),
    path('product/<int:id>/', views.ProductDetails.as_view()),
    path('collection/', views.collection_list),
    path('collection/<int:pk>/', views.collection_deatil, name="collection_deatil")
]