from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf

import datetime
import stripe

from accounts.models import User
from purchase.forms import AddressForm, CCRegistrationForm


@login_required() 
def address(request):

    #If form being submitted (Posted) then check info
    if request.method == 'POST':
        form = AddressForm(request.POST)
        #validate form and if OK, save details to database 
        if form.is_valid():
            user = get_object_or_404(User, username=request.user)
            user.address_line1 = form.cleaned_data['address_line1']
            user.address_line2 = form.cleaned_data['address_line2']
            user.county = form.cleaned_data['county']
            user.postcode = form.cleaned_data['postcode']
            user.save()
            messages.success(request, "Address successfully updated")
            #once updated, send user to profile page
            return redirect(reverse('profile'))
        
        else:
            #inform user why form was rejected
            messages.error(request, "Either incorrect postcode or non alpha-numerics used to complete address details, please re-enter")

    else:
        form = AddressForm()

    form = AddressForm()
    args = {'form':form}    
    return render(request, 'purchase/address.html', args)



@login_required() 
def register_cc(request):

    #If form being submitted (Posted) then check info
    if request.method == 'POST':
        form = CCRegistrationForm(request.POST)

        #create stripe_id for this checkout
        if form.is_valid():
            data = form.cleaned_data
            user = get_object_or_404(User, username=request.user)

            #create customer on stripe, this creates a customer token on stripe that 
            #is re-useable rather than one off transational token
            stripe_customer = stripe.Customer.create(
            email=user.username,
            source=data['stripe_id'],
            )

            #save stripe credit card token to database for future sure checkouts
            user = User.objects.filter(username=request.user).update(stripe_custID = stripe_customer.id)
            #inform user
            messages.success(request, "Credit Card successfully updated")
            #once updated, send user to profile page
            return redirect(reverse('profile'))

    else:
        today = datetime.date.today()
        form = CCRegistrationForm()
 
    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))
 
    return render(request, 'purchase/register_cc.html', args)
