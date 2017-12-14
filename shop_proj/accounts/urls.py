from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),   
    url(r'^logout/$', views.logout, name='logout'),    
    url(r'^user_register/$', views.user_register, name='user_register'),
]


