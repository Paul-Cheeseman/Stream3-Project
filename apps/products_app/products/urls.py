from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.products, name='products'),
    url(r'^detail/$', views.product_detail, name='product_detail'),    

]


