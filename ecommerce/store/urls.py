from django.urls import include,path
from django.urls import path
from . import views


urlpatterns=[
    path('', views.store , name="store"),
    path('cart/', views.cart , name="cart"),
    path('create/', views.product_create , name="create"),
    path('<pk>/delete/', views.ProductDeleteView.as_view() , name="delete"),
    path('checkout/' , views.checkout, name="checkout"),
    path('update_item/' , views.updateitem, name="update_item"),
    
]