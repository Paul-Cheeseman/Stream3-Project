# Code Institute Stream 3 Project

## Overview
This code is for a site that is required for the Code Institute end of Stream 3 (Full Stack Frameworks) project. It is to demonstrate an ability to code, test and deploy (to GitHub) a full stack website that follows good practice. The website has the dual purpose of covering examination requirements while also illustrating my level of knowledge/competency to prospective employers.


## Functionality of the project
- List all functions of cart
- Orders, can list and see
- Pagination implemented
- Set up perminant stripe access for customer via stripe API (stored perminant token in db)
- The stock level limit (ALSO STOCK LEVEL MUST BE REDUCED ON ORDERS)
- The database management with regard to expired annonymous session (PUT IN THE CODE)
- The code to switch the annonymous session to signed in user (PUT IT IN!)
- Safety, can't checkout without an address or credit card
- Mention where I have put required JavaScript for project
- Mention about it being "app-ified" - DO IT
- If stock level has reduced since last log in, if a customer has a stored cart, the item is removed from the cart and customer informed.
- If at checkout and stock levels have changed, adjustments made to stock and delivery and highlighted to customer


MENTION THAT IMAGES AND TEXT ARE CURRENTLY JUST PLACEHOLDING, SO QUALITY MIGHT NIT BE THERE


- mention claen structure, shop_proj, core app, then accompanying apps (to keep shop level views (index etc) in a tidy place)

 - mention that he reuasable apps are in folder

- Responsive design etc, what were my additions?
- Made the admin panels more user friendly by adjusting layout
- Validation and defensive approach on admin panel, either predefined dropdown lists used to ensure consitentsy of input, plus the stock level is checked to ensure it is a value over 0

 - It will be a rule of using the app(s) that the products are never deleted, this si so that the ordering system has access to all historical products and also so that any retrieved cart is ensured to have the product to reference, even if in stock or not. SO THE ADMIN PANEL HAS BEEN PREVENTED FROM DELETING PRODUCTS to ensure the app runs smoothly


- Licence open source, used:
https://opensource.org/licenses/BSD-3-Clause


## Project Coding
#### Technologies used
- HTML
- CSS
	- [Bootstrap](http://getbootstrap.com/)
- JavaScript
 	- jQuery
- Python (https://www.python.org/)
	- Django Framework (https://www.djangoproject.com/)

#### Coding concepts used/followed
nnnnnnnnnn

#### 3rd party code used:
- I used these on which to base my site, although I have altered in substantially.
	https://themefisher.com/products/sulfur-free-simple-html-template/
	MENTION THIS IS TO NOT REINVENT THE WHEEL, the base functionality is was I was after
	 - I have used by on tables and buttons (products page)
	 - I have used by own forms (address/cc)
	 - I have put in own button disable functionality (checkout)
	 - I have put in own table row highlight (css)
	 - I have added ability to select a row of table for product to show product detail page, plus changing pointer to finger to help users
	 - I have added selection on tables, also jQuery to store the values seletced locally so that they are retained as shown filter/search selections

Timmy (Mentor) supplied some of the code for orders (To get date/order-id and totals)

These are examples of not re-inventing the wheel!

- for alert on logout:
https://sweetalert.js.org/guides/

- I have used Easy Thumbnails (easy-thumbnails (2.5) https://easy-thumbnails.readthedocs.io/en/2.1/install/ and configured in to use particular sizes.

 - I have used https://gist.github.com/benbacardi/d6cd0fb8c85e1547c3c60f95f5b2d5e1 to help with implementing multiple filter application for the Products page, as it requires remembering the previous URLS sent.

- stripe (1.73.0), this is probably worth a mention by itself

- Font-awesome for most icons
- Linecons for t-shirt

jQuery code within the stripe.js file within the purchase app, is code supplied by the Code Institute https://www.codeinstitute.net/

Login/logout app, it is based on code supplied by the Code Institute https://www.codeinstitute.net/ but has been changed, outline how!


Django (1.11.7)
django-bootstrap-forms (0.1)
django-forms-bootstrap (3.1.0)
django-paypal (0.4.1)
Pillow (4.3.0)



#### Justification of approach
- **** While cart based apps were available, I wanted to develop my own so that I had the opportunity to develope from "the ground up", and alo it would allow me to tailor the app to my specific requirements.
This can be evidenced through my GIT history.

For this project I haven't set up a secure page (HTTPS) for the credit card information as it is only currently a test site. Should I move this project into a production/live ennvironment I would ensure it was because I recognise it is a security risk (due to packet sniffing etc) to send this type of sensitive information across a non-encrypted connection.


## How was the project deployed
- 

## How was the project tested
- 

## How to set up the project locally
---------------------------------------------
THIS NEEDS TIDYING UP!!!!
- Clone the repo Paul-Cheeseman/Stream3-Project
- Create and install a virtualenv in a suitable place:
	- Find a suitable dir to create it
	- enter command: virtualenv shop_proj
	- cd to source env/bin/activate 
	- enter command: activate
	- go to requirements.txt, enter: pip install requirements.txt
	- migrate the python files, python manage.py migrate
    - Run tests: python manage.py test
    - Run server: python manage.py runserver
---------------------------------------------

### Testing code quality
I validated the HTML used through https://validator.w3.org

I rendered each page in a browser, saved the page, then copied the HTML into the validator
My aim was to ensure no errors, some warnings persist, some of these were layout issues (sections not having headings, WHY) and also a 3rd party script (SweetAlert) raised a warning.


### Testing Responsive Design:
I have tested the website, across different devices, different browsers and different Operating Systems, to ensure that the site adapts cleanly/neatly to the different device criteria, summary of what I tested is below (limited to what I had available):
- iPhone: Firefox, Chrome, Opera
- Samsung phone: Firefox, Chrome, Opera
- iPad: Firefox, Chrome, Opera
- Laptop Win10: Firefox, Chrome, Opera (resizing browser window to check scalability)
- Desktop OS X Mavericks: Firefox, Chrome, Opera (resizing browser window to check scalability)

- MENTION IN HERE THE UNIT TESTS THROUGH Django

### Functional Testing
The key elements of the testing were the different aspects of the "user story", which in essence was checking that the functionality that the user would need to use to achieve their goal, in this case looking at my photos and finding out a bit about me) worked, so I checked: 
 - PUT IN THE TESTS!!!!


