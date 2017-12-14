==========
 Cart
==========
 
Cart is a reusable cart app for Django
 
It is designed to add, remove and list items for annonymous users within a session variable

The app requires 


Quick start
-----------
 
1. Add 'cart' to your INSTALLED_APPS setting like this::
 
    INSTALLED_APPS = (
        ...
        'cart',
    )
 
2. Include the checkout URLconf in your project urls.py like this::
    url(r'^cart/', include('cart.urls')),

3. Add a link to the cart in the base.html template
	<li><a href="{% url 'cart_list' %}">Cart</a></li>
 
3. Add a link to the cart in the base.html
	<li><a href="{% url 'cart_list' %}">Cart</a></li>

4. Add a link to update the cart in the items/product listing/purchasing template
	action="{% url 'cart_add' %}"


4. Visit http://127.0.0.1:8000/cart/cart_list to list the cart contents, although unless a cart has items/products in it, it won't list information.