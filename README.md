# Code Institute Stream 3 Project

## Overview
This site has been developed for the Code Institute end of Stream 3 (Full Stack Frameworks) project. It is to demonstrate an ability to code, test and deploy (to Heroku) a full stack website that follows good practice. The website has the dual purpose of covering examination requirements while also illustrating my level of knowledge/competency to prospective employers.

The site is a shop which sells products and advertises services for a small family bespoke clothing and tailoring business. A critical part of the brief was to design a stock management system which wouldn't allow users to order more than is currently in stock at a given time so the business can always meet customer requirements/expectations regarding delivery. Functionality to achieve real-time pre-checkout stock management for multiple customers has been incorporated into the design. For example imagine customer1 has a given amount of a particular item in their basket. Then while they continue to shop on the site customer2 completes a purchase of an amount of the same product which results in their now not being enough stock to honour customer1's order. When customer1 is at the checkout and goes to complete the purchase the system checks the stock and finds the discrepancy. It then amends customer1's order to reflect the maximum amount of the product left in stock, alerts customer1 that their order has been amended, gives the reason for the amendment, and issues a requested to contact the business if they would like to order more than is currently in stock. Please check the accompanying documentation for more details on the design decisions.

The clients wanted primarily mobile devices and were not too bothered about large screen PC's as they envisioned most of the customers on laptops, tablets or phones (as shown in the customer profiling in the additional documents submitted).

- Licence: open source, used:
https://opensource.org/licenses/BSD-3-Clause


## Functionality of the project
- Accounts
	- User sign-up/registration
	- User authentication system
    - Login, handles attempt at duplicate name sign-up gracefully

- Cart
	- Add/remove and list items in cart
	- Option to save current cart and resume with it a next login
		- If cart previously saved, on subsequent sign-in cart checked to see if current stock levels can still honour 	each cart item order, if not the given items are removed and customer informed.
		- If a user signs in with an session cart active but a cart stored from the previous session, the current session cart is used, the previously stored cart removed, and customer informed.
	- If a anonymous user signs-in (or signs-up) the current session cart is associated with user account giving a seamless transition for user.
	- Cart badge colour coded (red/green to show signed in/out), cart badge shows quantity of items ordered.

- Checkout
	- If stock levels change in between the customer putting in cart and the checkout (another customer order may reduced stock levels) the customer the order is recalculated to current stock levels and customer informed of change.
	- Can't checkout without an address or credit card having been registered.

- Core
	- Contact page has a JavaScript validated 'deadline date' field on the contact form to ensure that valid details are entered. 
	- Login icon colour coded (red/green to show signed in/out).

- Orders
	- Listing of all orders made for a registered customer
		- Uses an ID along with the time and date to identify order, meaning can cater for multiple orders from same customer in same day
		- Orders listed chronologically with last order first to enable easier checking for customers on recent orders
	- Each listing is linked to the details of the specific order
	- Pagination (triggered on over 10 orders listed) implemented for better usability

- Products
	- Product listing - Multiple filtering on products to given granularity when searching
	- Product detail - if the customer tries to purchase more than is in stock, customer told how many in stock and then that limit is imposed on order value to prevent purchase of unstocked items (as per client requirements). 
	 - Click selection on product table rows gives the products detail page
	 - jQuery stores filtering values/selections so that they are retained across server calls
	- Product detail - if product out of stock, the input box for entering the amount of items to order is removed and an 'out of stock' message presented to customer
	- Pagination implemented (triggered on over 5 items listed) for better usability

- Purchase
	- When customer registers a credit card a stripe token for it created (via the stripe API) and stored in the database. This means when the user subsequently signs-in they can checkout without inputting card details (and their card details are not stored in this sites database).
	- Customer can only use alpha-numerics and spaces in address fields (mentor said that was enough validation)


- General
	- Uses easythumbnails, so it is uses smaller size (in bytes) images for smaller devices, making it responsive plus more data efficient
	- The admin panels have been customised and made more user friendly for the administrator(s)
	- Validation and defensive approach on admin panel, predefined drop-down lists used to ensure consistency of input and the stock level is checked to ensure it is a value over 0



## Project Coding
#### Technologies used
- HTML
- CSS
	- [Bootstrap](http://getbootstrap.com/)
- JavaScript
 	- jQuery
 	- Jasmine (https://jasmine.github.io/)
- Python (https://www.python.org/)
	- Django Framework (https://www.djangoproject.com/)


#### 3rd party code used:
- https://themefisher.com/products/sulfur-free-simple-html-template/ I used this as a base theme but have altered in substantially removing large sections and redesigning a lot of it. I have extended it too in various ways. A couple of examples are adding the ability to highlight and select a row of the products/orders table to show the details page, plus changing the mouse pointer to a finger to help users identify an active link on table rows.

- https://sweetalert.js.org/guides/ This is the core of the code that generates the alert on logout, although I have adapted it so that it redirects a user to the logout view and also triggers, if required, subsequent code that will store the cart in the database.

- Easy Thumbnails (easy-thumbnails (2.5) https://easy-thumbnails.readthedocs.io/en/2.1/install/ to manages the size of images files (so larger graphics files are only sent when really needed, saving bandwidth) and configured in settings.py to use a range of dimensions to cater for different devices screen sizes.

- I used https://gist.github.com/benbacardi/d6cd0fb8c85e1547c3c60f95f5b2d5e1 to help with implementing multiple filter application for the Products page as it requires remembering the previous URLS sent. I have had to further develop the code so that it ignores the 'page' value put into the URL by pagination.

- Font-awesome for most icons
	http://fontawesome.io/

- Linecons for t-shirt icon
	https://designmodo.com/linecons-free/

 - jQuery code within the stripe.js file within the purchase app, is code supplied by the Code Institute https://www.codeinstitute.net/

 - The register/login/logout views within accounts app, it is based on code supplied by the Code Institute https://www.codeinstitute.net/ but has been changed substantially. For example the register views now gracefully handles attempts to register a username already in use, the login app now checks for a stored cart from a the last login and if present restores it, the logout app now stores a cart if required.


#### Justification of approach
While a few shop based apps/tutorials were available I couldn't find one with the functionality I required, especially around the strict stock management requirements from my client. Due to this I have written the whole site from scratch so that it could fully accommodate my clients requirements. This approach had the added benefit of requiring me to understand more Python and Django than I would otherwise have needed to.

Also, for this project I haven't set up a secure page (HTTPS) for the credit card information as it is only currently a test site. Should I move this project into a production/live environment I would ensure it was because I recognise it is a security risk (due to packet sniffing) to send this type of sensitive information across a non-encrypted connection.


## How was the project deployed
-------------------------------
- Clone the repo https://github.com/Paul-Cheeseman/Stream3-Project to a dir of your choice 
- Install virtualenv software if required https://docs.python.org/3/tutorial/venv.html
- Go to the dir where you want to install your virtualenv, then:
	C:\your-desired-folder>mkdir virtualenv
	C:\your-desired-folder>cd virtualenv
	C:\your-desired-folder\virtualenv>virtualenv shop_proj
	C:\your-desired-folder\virtualenv>cd scripts
	C:\your-desired-folder\virtualenv\scripts> activate
- Within the virtualenv go to shop_proj dir within the downloaded repo:
	C:\.........\shop_proj>pip install requirements.txt
- Migrate the python files:
	C:\.........\shop_proj>python manage.py migrate
- Run tests: 
	C:\.........\shop_proj>python manage.py test
- Run server to activate site: 
	C:\.........\shop_proj>python manage.py runserver


## How was the project tested
The project was tested in a variety of ways.

### Testing HTML quality
HTML validated through https://validator.w3.org

### Django Unit Testing:
Unit Testing (testing specific modules/functions of code) has been carried out to some degree on all sections of the sites code. The 'test' file within each app lists the tests that have been created and each of those tests will will not only check functionality for this current release, they will form the basis of future regression testing which will check if/how subsequent software impacted the sites.

It is worth noting that the cart function was deemed an integral part of the site which would need to be used by the majority of the sites other core functionality. Because of this the cart function was rewritten to be more modular in design, allowing better reuse of code and enabled unit testing of specific functions within the module rather than just checking the correct resolving of URLs and testing aspects of the http response. 

### JavaScript Unit Testing:
The only JavaScript suitable for testing was related to the form on the contact page, the code being tested and jasmine files can be found within the js_testing files within the shop_proj directory.


### Functional Testing:
Functional Testing (which testing specific aspects of functionality across the whole system) has been carried out manually and the tests are listed in the accompanying documentation.


### Usability Testing:
Usability Testing (evaluating a product by testing it on user) has been carried out by the clients, friends and family, each asked to use the site as they would other online retail sites. In addition each was asked to specifically test the product filtering, stock level management and cart retention between login's along with being asked to try and make the site make a mistake.


### Compatibility Testing:
I have tested the website, across different devices, different browsers and different Operating Systems, to ensure that the site adapts cleanly/neatly to the different device criteria, a summary of what I tested is within the accompanying documentation.
