from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.orders_list, name='orders'),
    url(r'^detail/$', views.orders_detail, name='orders_detail'),        
]


