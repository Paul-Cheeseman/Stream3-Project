==========
Purchase
==========
 
Purchase is a reusable cart app for Django
 
It is designed to register, and store in a database, two essential peices of information for online product purchase, a delivery address and payment medium (in this case stripe).

The app requires django-forms-bootstrap to manage the form layout.


Quick start
-----------
 
1. Add 'purchase' to your INSTALLED_APPS setting like this::
 
    INSTALLED_APPS = (
        ...
        'purchase',
    )
 
2. Include the checkout URLconf in your project urls.py like this::
    url(r'^purchase/', include('purchase.urls')),

3. Add a link to the credit card registration in the base.html template
	<li><a href="{% url 'register_cc' %}">Credit Card Register</a></li>

4. Add a link to the address input form in the base.html template
    <li><a href="{% url 'address' %}">Add Address</a></li>

5. Visit http://127.0.0.1:8000/purchase/register_cc/ to see the credit card registration page, or http://127.0.0.1:8000/purchase/address/ for the registration page.