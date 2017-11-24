"""shop_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import views as accounts_views
#from shop import views as shop_views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from products import views as product_views
from cart import views as cart_views
from orders import views as orders_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', cart_views.get_index, name='index'),
    url(r'^cart_list', cart_views.cart_list, name='cart_list'),
    url(r'^cart_add', cart_views.cart_add, name='cart_add'),
    url(r'^cart_update', cart_views.cart_update, name='cart_update'),
    url(r'^cart_del', cart_views.cart_del, name='cart_del'),

    url(r'^products/$', product_views.products, name='products'),

    url(r'^checkout/$', cart_views.checkout, name='checkout'),

    url(r'^address/$', accounts_views.address, name='address'),

    url(r'^orders/$', orders_views.orders_list, name='orders'),
    
    url(r'^test', cart_views.cart_add, name='contact'),
#	url(r'^index/$', shop_views.get_index),
    url(r'^user_register/$', accounts_views.user_register, name='user_register'),
    url(r'^register_cc/$', accounts_views.register_cc, name='register_cc'),    
#    url(r'^contact/$', shop_views.get_contact, name='contact'),    
	url(r'^profile/$', accounts_views.profile, name='profile'),	
	url(r'^login/$', accounts_views.login, name='login'),	
	url(r'^logout/$', accounts_views.logout, name='logout'),	
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),	

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
   import debug_toolbar
   urlpatterns += [
       url(r'^__debug__/', include(debug_toolbar.urls)),
   ]
