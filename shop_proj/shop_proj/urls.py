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
from shop import views as shop_views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from products import views as product_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', shop_views.get_index, name='index'),
	url(r'^user_register/$', accounts_views.user_register, name='user_register'),
    url(r'^register_cc/$', accounts_views.register_cc, name='register_cc'),    
	url(r'^profile/$', accounts_views.profile, name='profile'),	
	url(r'^login/$', accounts_views.login, name='login'),	
	url(r'^logout/$', accounts_views.logout, name='logout'),	
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),	
    url(r'^products/$', product_views.all_products),
    url(r'^basket_add/$', product_views.basket_add, name='basket_add'),
    url(r'^basket_list/$', product_views.basket_list, name='basket_list'),    
    url(r'^sort_prod_alpha/$', product_views.sort_prod_alpha, name='sort_prod_alpha'),
    url(r'^sort_prod_price/$', product_views.sort_prod_alpha, name='sort_prod_price'),    
    url(r'^filtered_cat/$', product_views.filtered_cat, name='filtered_cat'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


