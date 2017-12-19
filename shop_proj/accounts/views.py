# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings


from accounts.forms import UserRegistrationForm, UserLoginForm
from accounts.models import User
from products.models import Product
from cart.models import Cart, CartItem

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
 
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))
 
            auth.login(request, user)
            messages.error(request, "You have successfully logged in")            
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
                            print("")
                            #Do nothing, the amount in stock can still cover order

                        else:
                            #remove cartItems from cart which their is now not enough stock to fulfill
                            CartItem.objects.filter(cart_id=cart, id=item.product_id).delete()
                            #msg user
                            cart_amended = True

                
                if cart_amended:
                    messages.error(request, "Your old cart has had at least one item removed due to a change in stock levels")

                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")
    else:
        form = UserLoginForm()

 
    args = {'form':form}
    args.update(csrf(request))
    return render(request, 'accounts/login.html', args)





@login_required(login_url='/login/')
def logout(request):

    if request.GET.get('cart_store') == "yes":

        if 'cart' in request.session:
            cart = request.session['cart']

            user = User.objects.get(username=request.user)
            user.saved_cart_id = cart
            user.save()

    else:

        user = User.objects.get(username=request.user)

       #set session cart from stored cart
        cart = Cart.get_cart(request.session['cart']) 
        cart_contents = cart.items_in_cart()

        if cart_contents:
            #delete all items in cart
            for item in cart_contents:
                #remove cartItems from cart which their is now not enough stock to fulfill
                cart.remove_from_cart(item.product_id)


        #set back to 0 so on login no attempt at retrieving a stored cart is made
        user.saved_cart_id = 0
        user.save()


        
    if request.session.get('cart'):
        #destroy cart session variable
        del request.session['cart']

    #log user out
    auth.logout(request)
    return redirect(reverse('index'))