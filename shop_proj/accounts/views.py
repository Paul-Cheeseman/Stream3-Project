# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.conf import settings
from accounts.forms import UserRegistrationForm, UserLoginForm
from accounts.models import User
from products.models import Product
from cart.models import Cart, CartItem

def user_register(request):
    if request.method == 'POST':

        if User.objects.filter(username=request.POST.get('email')).exists():
            messages.error(request, "The username {0} already exists, please choose another one".format(request.POST.get('email')))

            form = UserRegistrationForm()
 
        else:
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
 
                user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

                auth.login(request, user)
                messages.success(request, "You have successfully logged in")            
                messages.info(request, "Please be aware you will need a credit card and address registered before you can complete any orders")
                return redirect(reverse('profile'))
 
    else:
        form = UserRegistrationForm()
 
    args = {'form': form}
    args.update(csrf(request))
 
    return render(request, 'accounts/user_register.html', args)





def profile(request):
    return render(request, 'profile.html')


def login(request):

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                    password=request.POST.get('password'))
 
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")


                #variable to see if old cart is changed after checking against current stock levels
                cart_amended  = False

                if user.saved_cart_id != 0:
                    
                    #set session cart from stored cart
                    request.session['cart'] = user.saved_cart_id
                    cart = Cart.get_cart(request.session['cart']) 
                    cart_contents = cart.items_in_cart()

                    #for item in
                    for item in cart_contents:
                        #check the associated product to see if its stock level is above the quantity
                        cart_queryset = Product.objects.filter(id=item.product_id, stock_level__gte=item.amount)
                        if  cart_queryset.exists():
                            print()
                            #Do nothing, the amount in stock can still cover order

                        else:
                            cart_amended = True
                            cart.remove_from_cart(item.product_id)


                
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
                    #messages.error(request, "The username {0} already exists, please choose another one".format(request.POST.get('email')))


                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")
    else:
        form = UserLoginForm()

 
    args = {'form':form}
    args.update(csrf(request))
    return render(request, 'accounts/login.html', args)





@login_required()
def logout(request):

    if request.GET.get('cart_store') == "yes":

        if 'cart' in request.session:
            cart = request.session['cart']

            user = User.objects.get(username=request.user)
            user.saved_cart_id = cart
            user.save()




    elif request.GET.get('cart_store') == "no":

       #set session cart from stored cart
        if request.session.get('cart'):
            #destroy cart session variable

            #This should remove the cart and its associated cart items from database 
            Cart.objects.get(id=request.session['cart']).delete()

            #set back to 0 so on login no attempt at retrieving a stored cart is made
            user = User.objects.get(username=request.user)
            user.saved_cart_id = 0
            user.save()

            del request.session['cart']

    #log user out
    auth.logout(request)
    return redirect(reverse('index'))