# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm, CCRegistrationForm
from django.contrib.auth.decorators import login_required

from accounts.models import User

# Create your views here.

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm, UserLoginForm, AddressForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
import datetime
import stripe



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
 
    return render(request, 'user_register.html', args)




stripe.api_key = settings.STRIPE_SECRET




@login_required(login_url='/login/') 
def register_cc(request):
    #The form sent to server
    if request.method == 'POST':

        print("request.POST:")
        print(request.POST)


        form = CCRegistrationForm(request.POST)

        #create stripe_id for this checkout
        if form.is_valid():
            data = form.cleaned_data
            #form.save(data['stripe_id'], request.user)

            user = User.objects.get(username=request.user)

            # ----------------------------------------------------------
            ### NEED TO PUT IN SOME CHECKING HERE TO VALIDATE CARD IS OK
            ### Also need to put in a DELETE ACCOUNT, and delete customer 
            #   from stripe DB along with own: https://stripe.com/docs/api#delete_customer
            # ----------------------------------------------------------

            #create customer on stripe
            stripe_customer = stripe.Customer.create(
            email=user.username,
            source=data['stripe_id'],
            )

            #save credit card to database for future sure checkouts
            user = User.objects.filter(username=request.user).update(stripe_custID = stripe_customer.id)
         


            #Change to a thankyou for logging in
            return redirect(reverse('profile'))


    else:
        today = datetime.date.today()
        form = CCRegistrationForm()
 
    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))
 
    return render(request, 'register_cc.html', args)






@login_required(login_url='/login/')
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
                messages.error(request, "You have successfully logged in")

                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")
    else:
        form = UserLoginForm()

 
    args = {'form':form}
    args.update(csrf(request))
    return render(request, 'login.html', args)



@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def address(request):

    if request.method == 'POST':
        form = AddressForm(request.POST)
        #data validated via JS

        user = User.objects.get(username=request.user)      
        user.address_line1 = request.POST['address_line1']
        user.address_line2 = request.POST['address_line2']
        user.county = request.POST['county']
        user.postcode = request.POST['postcode']
        user.save()

        messages.error(request, "Address successfully updated")

    else:
        form = AddressForm()

    form = AddressForm()
    args = {'form':form}    
    return render(request, 'address.html', args)