==========
 Orders
==========
 
Orders is a reusable order listing app for Django
 
It is designed to 

The app requires 

 
Quick start
-----------
 
1. Add 'orders' to your INSTALLED_APPS setting like this::
 
    INSTALLED_APPS = (
        ...
        'orders',
    )
 
2. Include the orders URLconf in your project urls.py like this::
 
    url(r'^orders/', include('orders.urls')),


3. Add a link to the checkout in the base.html
	<li><a href="/orders/">Orders</a></li>
 
3. Visit http://127.0.0.1:8000/orders/ to view the orders page, although unless at least one order has been logged in the batatabase it won't list information.