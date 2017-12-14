==========
 Checkout
==========
 
Checkout is a reusable checkout app for Django
 
It is designed to bridge the gap between a users cart, a stripe payment and logging the purchase(s) within and orders model.

The app requires the user to have an address and a stripe customer token stored within the purchasing user account before payment will be made and the order will be logged..
 
Quick start
-----------
 
1. Add 'checkout' to your INSTALLED_APPS setting like this::
 
    INSTALLED_APPS = (
        ...
        'checkout',
    )
 
2. Include the checkout URLconf in your project urls.py like this::
    url(r'^checkout/', include('checkout.urls')),

3. Add a link to the checkout in the base.html
	<li><a href="/checkout/">Checkout</a></li>
 
4. Visit http://127.0.0.1:8000/checkout/ to view the checkout page, although unless a cart is created it 	won't list information.