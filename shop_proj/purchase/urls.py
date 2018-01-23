from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^address/$', views.address, name='address'),
    url(r'^register_cc/$', views.register_cc, name='register_cc'),    
]


