from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^checkout/$', checkout_views.checkout, name='checkout'),
    url(r'^/$', views.checkout, name='checkout'),    
]


