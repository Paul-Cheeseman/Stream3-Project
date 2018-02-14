# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm
from accounts.models import User
from cart.models import Cart, CartItem
from products.models import Product



def user_register(request):
    #If the request method is POST the form is being submitted
    if request.method == 'POST':
        #Check if the user name/email already exists, if so then let user know gracefully
        if User.objects.filter(username=request.POST.get('email')).exists():
            messages.error(request, "The username {0} already exists, please choose another one".format(request.POST.get('email')))
            #Reset form
            form = UserRegistrationForm()
        else:
            #If the user name/email is unique, check form information is valid
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                #Save form information to database
                form.save()
                #Use the credentials to log user in
                user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password1'))
                auth.login(request, user)
                messages.info(request, "Please be aware you will need to add a credit card and address to your profile before you can complete any orders")
                #Send user to Profile page
                return redirect(reverse('profile'))
    else:
        #If the request method is NOT POST, then the page needs to rendered as a fresh page
        form = UserRegistrationForm()
    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'accounts/user_register.html', args)



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password'))
 
            #Accept user if valid credentials
            if user is not None:
                auth.login(request, user)

                #variable to see if old cart is changed after checking against current stock levels
                cart_amended  = False

                #check if cart id stored for this user in db (from previous session)
                if user.saved_cart_id != 0:

                    #check if the user has already created a cart by adding one or more products, if they have then
                    #stored cart is of no use (as they have presumably forgotten they stored) and should be binned
                    if 'cart' in request.session:
                        
                        #if they have, hold the current cart num so subsequent del_cart doesn't remove (as it clears the
                        #request.session['cart']), delete the stored cart and then re-apply the recently created cart 
                        #reference to the request.session['cart'] variable
                        hold_cart_num = request.session['cart']

                        #switch to old cart in session to remove everything cleanly
                        request.session['cart'] = user.saved_cart_id
                        #get stored cart and remove
                        cart = Cart.get_cart(request.session['cart']) 
                        cart.del_cart(request)

                        #switch back to use new/current cart
                        request.session['cart'] = hold_cart_num

                        #let user know
                        messages.info(request, "Your current cart has replaced the cart you stored on your last visit")
    
                    else:

                        #set session cart from stored cart
                        request.session['cart'] = user.saved_cart_id
                        cart = Cart.get_cart(request.session['cart']) 
                        cart_contents = cart.items_in_cart()

                        if cart.amount_items_in_cart() > 0:
                            #check the associated product to see if its stock level is above the quantity
                            for item in cart_contents:
                                #pull product from model if the stock level is greater than or equal to desired value
                                #to ensure stock levels
                                cart_queryset = Product.objects.filter(id=item.product_id, stock_level__gte=item.amount)
                                #if no queryset produced, then at lease one item isn't at the right value, to save 
                                #complications remove whole basket
                                if not cart_queryset.exists():
                                    cart_amended = True
                                    cart.remove_from_cart(item.product_id)
                        #let user know
                        if cart_amended:
                            messages.error(request, "Your old cart has had at least one item removed due to a reduction in stock levels")
                        else:
                            messages.info(request, "The cart you stored at the end of your previous session has been restored")
                
                #Inform User that Address and/or Credit Card are required before oder can be completed
                user = get_object_or_404(User, username=request.user)
                if user.stripe_custID == "None" or (user.address_line1 == "None" and user.postcode == "None"):
                    cc_address_reg_msg = ""
                    if user.stripe_custID == "None" and user.address_line1 == "None" and user.postcode == "None":
                        cc_address_reg_msg = "credit card and address"
                    elif user.stripe_custID == "None":
                        cc_address_reg_msg = "a credit card"
                    else:
                        cc_address_reg_msg = "an address"

                    messages.info(request, "Please be aware you will need {0} registered before you can complete any orders".format(cc_address_reg_msg))
                return redirect(reverse('profile'))
            else:
                #tell user if they could not be authenticated
                form.add_error(None, "Your email or password was not recognised")
    else:
       #If the request method is NOT POST, then the page needs to rendered as a fresh page
        form = UserLoginForm()

    args = {'form':form}
    args.update(csrf(request))
    return render(request, 'accounts/login.html', args)





@login_required()
def logout(request):

    #determine if cart needs to be stored
    if request.GET.get('cart_store') == "yes":

        cart = Cart.objects.get(id=request.session['cart'])
        #Check if the customer is confused and trying to save an empty cart, just delete it if so
        #and set saved_cart_id back to 0
        if cart.amount_items_in_cart() == 0:
            Cart.objects.get(id=request.session['cart']).delete()
            user = User.objects.get(username=request.user)
            user.saved_cart_id = 0
            user.save()
        #store cart reference in the database
        elif 'cart' in request.session:
            cart = request.session['cart']
            user = User.objects.get(username=request.user)
            user.saved_cart_id = cart
            user.save()


    elif request.GET.get('cart_store') == "no":

        if request.session.get('cart'):
            #This removes the cart and its associated cart items from database 
            #(Django will remove associated foreign key items when primary key deleted)
            Cart.objects.get(id=request.session['cart']).delete()

            #set user associated cart ref back to 0 (so on login no attempt at retrieving a stored cart is made)
            user = User.objects.get(username=request.user)
            user.saved_cart_id = 0
            user.save()

            #remove cart from request.session to give a 'fresh start'
            del request.session['cart']

    #log user out
    auth.logout(request)
    return redirect(reverse('index'))