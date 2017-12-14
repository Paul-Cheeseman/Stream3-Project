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
from products import views as product_views
from cart import views as cart_views
from checkout import views as checkout_views
from orders import views as orders_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', cart_views.get_index, name='index'),

    url(r'^new_index', cart_views.get_new_index, name='new_index'),


    url(r'^checkout', include('checkout.urls')),
    url(r'^orders/', include('orders.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^purchase/', include('purchase.urls')),
    url(r'^products/', include('products.urls')),
    
    url(r'^test', cart_views.cart_add, name='contact'),
	url(r'^profile/$', accounts_views.profile, name='profile'),	

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
   import debug_toolbar
   urlpatterns += [
       url(r'^__debug__/', include(debug_toolbar.urls)),
   ]
