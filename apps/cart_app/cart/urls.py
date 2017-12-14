from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cart_list', views.cart_list, name='cart_list'),
    url(r'^cart_add', views.cart_add, name='cart_add'),    
]


