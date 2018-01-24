from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^contact/$', views.get_contact, name='contact'),
	url(r'^profile/$', views.get_profile, name='profile'),	
	url(r'^services/$',views.get_services, name='services'),
]


