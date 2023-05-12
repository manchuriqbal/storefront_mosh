from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('product/', views.product_list),
    path('product/<int:id>/', views.product_details)
]