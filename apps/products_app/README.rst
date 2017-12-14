
==========
Products
==========
 
Products is a reusable cart app for Django
 
It is designed to list the products sorted in the database, filter them on specific parameters and launch a product detail page for each product listed. Both the product list and the product detail pages allow the customer to add the product (in the quantity they desire) to a cart or remove it.


Quick start
-----------
 
1. Add 'products' to your INSTALLED_APPS setting like this::
 
    INSTALLED_APPS = (
        ...
        'products',
    )
 
2. Include the checkout URLconf in your project urls.py like this::
    url(r'^products/', include('products.urls')),

3. Add a link to products in the base.html template
	<li><a href="{% url 'products' %}">Products</a></li>

4. Visit http://127.0.0.1:8000/products/list/ to see the products list (if no products in databaase nothing will be displayed).