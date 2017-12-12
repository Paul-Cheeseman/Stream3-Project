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
- Customer account removal
- Responsive design etc, what were my additions?


## Project Coding
#### Technologies used
- HTML
- CSS
	- [Bootstrap](http://getbootstrap.com/)
- JavaScript 
- Jasmine (https://jasmine.github.io/)
- Python (https://www.python.org/)
	- Django Framework (https://www.djangoproject.com/)

#### Coding concepts used/followed
nnnnnnnnnn

#### 3rd party code used:
- I used these on which to base my site, although I have altered in substantially.
	https://themefisher.com/products/sulfur-free-simple-html-template/
	MENTION THIS IS TO NOT REINVENT THE WHEEL, the base functionality is was I was after

- I have used Easy Thumbnails (easy-thumbnails (2.5) https://easy-thumbnails.readthedocs.io/en/2.1/install/ and configured in to use particular sizes.

 - I have used https://gist.github.com/benbacardi/d6cd0fb8c85e1547c3c60f95f5b2d5e1 to help with implementing multiple filter application for the Products page, as it requires remembering the previous URLS sent.

- stripe (1.73.0), this is probably worth a mention by itself


Django (1.11.7)
django-bootstrap-forms (0.1)
django-forms-bootstrap (3.1.0)
django-paypal (0.4.1)
Pillow (4.3.0)



#### Justification of approach
- **** While cart based apps were available, I wanted to develop my own so that I had the opportunity to develope from "the ground up", and alo it would allow me to tailor the app to my specific requirements.
This can be evidenced through my GIT history.




## How was the project deployed
- 

## How was the project tested
- 

### Testing code quality
I validated the HTML used through https://validator.w3.org

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


