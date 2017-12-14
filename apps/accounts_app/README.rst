==========
 Accounts
==========
 
Accounts is a reusable cart app for Django
 
It is designed to register new users and login/logout, it is based on code supplied by the Code Institute https://www.codeinstitute.net/ although has been adpated.

The app requires django-forms-bootstrap to manage the form layout.


Quick start
-----------
 
1. Add 'accounts' to your INSTALLED_APPS setting like this::
 
    INSTALLED_APPS = (
        ...
        'accounts',
    )
 
2. Include the checkout URLconf in your project urls.py like this::
    url(r'^accounts/', include('accounts.urls')),

3. Add a link to the registration in the base.html template
	<li><a href="{% url 'user_register' %}">Register</a></li>

4. Add a link to the login in the base.html template
    <li><a href="{% url 'login' %}">Login</a></li>

5. Add a link to the logout in the base.html template
 	<li><a href="{% url 'logout' %}">Log Out</a></li>

6. Visit http://127.0.0.1:8000/accounts/login/ to see the login page, or http://127.0.0.1:8000/accounts/	register/ for the registration page.