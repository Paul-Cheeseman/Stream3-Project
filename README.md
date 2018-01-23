# Code Institute Stream 3 Project

## Overview
This code is for a site that is required for the Code Institute end of Stream 3 (Full Stack Frameworks) project. It is to demonstrate an ability to code, test and deploy (to GitHub) a full stack website that follows good practice. The website has the dual purpose of covering examination requirements while also illustrating my level of knowledge/competency to prospective employers.

The site is a shop which sells products and advertises services for a small family bespoke clothing and tailoring business. A critial part of the brief was to design a basic stock management system which wouldn't allow users to order more than is currently in stock, if they wanted to order more than that, then they would need to contact the compnay to discuss the order. Functionality to achieve this has been incorporated into the design.

The clients wanted primarily mobile devices and were not too bothered about large screen PC's as they envisinged most of the customers on laptops, tablets or phones (as shown in the customer profiling in the additional documents submitted).

- Licence open source, used:
https://opensource.org/licenses/BSD-3-Clause



## Functionality of the project
- Accounts
	- User sign-up/registeration
	- User authentication system

- Cart
	- Add/remove and list items in cart
	- Option to save current cart and resume with it a next login
		- 	If cart previously saved, on subsequent sign-in cart checked to see if current stock levels can still honour 	each cart item order, if not the given items are removed and customer informed.
		- If a user signs in with an session cart active but a cart stored from the previous session, the current session cart is used, the perviously stored cart removed, and customer informed.
	- If a annonymous user signs-in (or signs-up) the current session cart is associated with user account giving a seemless transition for user.
	- Cart badge colour coded (red/green to show signed in/out), cart badge shows quantity of items ordered.


- Checkout
	- If stock levels change inbetween the customer putting in cart and the checkout (another customer order may reduced stock levels) the customer the order is recalulated to current stock levels and customer informed of change.
- Can't checkout without an address or credit card having been registered 

- Core
	- Contact page has a JavaScript validated 'deadline date' field on the contact form to ensure that valid details are entered. 
	- Login icon colour coded (red/green to show signed in/out).

- Orders
	- Listing of all orders made for a regstered customer
		- Uses an ID along with the time and date to identify order, meaning can cater for multiple orders from same customer in same day
		- Orders listed chronologically with last order first to enable easier checking for customers on recent orders
	- Each listing is linked to the details of the specific order
	- Pagination implemented for better usability

- Products
	- Producting listing - Multiple filtering on products to given granularity when searching
	- Product detail - if the customer tries to purchase more than is in stock, customer told how many in stock and then that limit is imposed on order input value to prevent purchase of unstocked items (as per client requirements). 
	 - I have added click selection on table rows, also jQuery to store the values seletced locally so that they are retained as shown filter/search selections
	- Product detail - if product out of stock then ordering input removed
	- Pagination implemented for better usability


- Purchase
	- When customer registers a credit card a stripe token for is created (via the stripe API) and stored in the database, meaning when the user subsequently signs-in they can checkout without inputting card details (and their card details are not stored in this sites database).
	- Customer can only use alph-numerics and spaces in address fields (mentor said that was enough validation)


 - Login, handles attempt at duplicate name sign-up gracefull
 - Product filtering (with multiple filters, filters which have titles that indicate they have been used etc), most filters have dropdown lists driven from database content so retricts maintenance overheads ensures those drop downs are always up to date
 

- General
	- Uses easythumbnails, so it is using smaller size (in bytes too!) images for smaller devices, making it response PLUS more data efficient (than just making a big photo look smaller (as the same data tranfer overhead as its still the orginally big pic)

	- Admin panels made more user friendly by putting in code to adjust the layout for administrator
	- Validation and defensive approach on admin panel, either predefined dropdown lists used to ensure consitentsy of input, plus the stock level is checked to ensure it is a value over 0



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
EXPLAIN HOW I HAVE ADAPTED EACH BIT

- I used this as a base theme but have altered in substantially removing large sections redesigning a lot of it. I have extended it too in various ways. A coupe of examples are adding the ability to highlight and select a row of the products/orders table to show the details page, plus changing pointer to finger to help users for an active link.
https://themefisher.com/products/sulfur-free-simple-html-template/
 
This is the core of the code that generates the alert on logout, although I have adapted it so that it redirects a user to the logout view and also triggers, if required, subsequent code that will store the cart in the database:
https://sweetalert.js.org/guides/

Easy Thumbnails (easy-thumbnails (2.5) https://easy-thumbnails.readthedocs.io/en/2.1/install/ to manages the size of images files (so larger grahics files are only sent when really needed, saving badnwdith) and configured in settings.py to use a range of dimensions to cater for different devices screen sizes.

I used https://gist.github.com/benbacardi/d6cd0fb8c85e1547c3c60f95f5b2d5e1 to help with implementing multiple filter application for the Products page as it requires remembering the previous URLS sent. I have had to further develop the code so that it ignores the 'page' value put into the URL by pagination.

- Font-awesome for most icons
	http://fontawesome.io/

- Linecons for t-shirt icon
	https://designmodo.com/linecons-free/

jQuery code within the stripe.js file within the purchase app, is code supplied by the Code Institute https://www.codeinstitute.net/

The register/login/logout views within accounts app, it is based on code supplied by the Code Institute https://www.codeinstitute.net/ but has been changed substantially. For example the register views now gracefully handles attempts to register a username already used, the login app now checks for a stored cart from a the last login and if present restores it, the logout app now stores a cart if required.



#### Justification of approach
While a few shop based apps/tutorials were available I couldn't find one with the functionality I required, especially around the strict stock ordering limitations. Due to this I have written the whole site from scratch so that it could fully accomodate my clients requirements. This had the added benefit of requiring me to understand more Python and Django than I would otherwise have needed to.

Also, for this project I haven't set up a secure page (HTTPS) for the credit card information as it is only currently a test site. Should I move this project into a production/live ennvironment I would ensure it was because I recognise it is a security risk (due to packet sniffing etc) to send this type of sensitive information across a non-encrypted connection.


## How was the project deployed
-------------------------------
- Clone the repo https://github.com/Paul-Cheeseman/Stream3-Project to a dir of your choice 
- Install virtualenv software if requrird https://docs.python.org/3/tutorial/venv.html
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
Unit Testing, testing specific modules/functions of code, has been carried out to some degree on all sections of the sites code. The 'test' file within each app lists the tests that have been created and each of those tests will will not only check functionality for this currecnt release, they will form the basis of future regression testing which will check if/how subsequent software impacted the sites.

It is worth noting that the cart function was deemed an integral part of the site which would need to be used by the majority of the sites other core functionality. Because of this the cart function was rewritten to be more modular in design, allowing better reuse of code and enabled unit testing of specific functions within the module rather than just checking the correct resolving of URLs and testing aspects og the http response. 

### JavaScript Unit Testing:
The only JavaScript suitable for testing was related to the form on the contact page, the code being tested and jasmine files can be found within the js_testing files within the shop_proj dierctory.


### Functional Testing:
Functional Testing, which is a type of black box testing, tests a slice of functionality of the whole system. This testing has been carried out manually, and the functional tests carried out are listed in the accompnaying documentation.


### Usability Testing:
Usability Testing, evaluating a product by testing it on user, has been carried out by friends and family, each asked to use the site as they would other online retail sites. In addition each was asked to specificly test the product filtering, stock level management and cart retention between login's along with being asked to try and make the site make a mistake.


### Compatibility Testing:
I have tested the website, across different devices, different browsers and different Operating Systems, to ensure that the site adapts cleanly/neatly to the different device criteria, summary of what I tested is below (limited to what I had available):
- iPhone: Firefox, Chrome, Opera
- Samsung phone: Firefox, Chrome, Opera
- iPad: Firefox, Chrome, Opera
- Laptop Win10: Firefox, Chrome, Opera (resizing browser window to check scalability)
- Desktop OS X Mavericks: Firefox, Chrome, Opera (resizing browser window to check scalability)
Please Note: The google mobile views don't do iphone 5 size etc and it seemed reasonable to take that as 

