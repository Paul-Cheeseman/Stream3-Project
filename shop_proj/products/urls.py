from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.products, name='products'),
    url(r'^detail/$', views.product_detail, name='product_detail'),    
    #url(r'^detail/?product_name=', views.product_detail, name='product_detail_stock_level'),    
]


