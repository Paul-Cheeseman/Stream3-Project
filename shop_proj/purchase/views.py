from django.shortcuts import render
from accounts.models import User
from django.contrib.auth.decorators import login_required
import datetime
from django.conf import settings
from django.template.context_processors import csrf
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import stripe
from django.core.urlresolvers import reverse

# Create your views here.

from purchase.forms import AddressForm, CCRegistrationForm



@login_required() 
def address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        #data validated via JS

        if form.is_valid():
            user = get_object_or_404(User, username=request.user)
            user.address_line1 = form.cleaned_data['address_line1']
            user.address_line2 = form.cleaned_data['address_line2']
            user.county = form.cleaned_data['county']
            user.postcode = form.cleaned_data['postcode']
            user.save()

            messages.success(request, "Address successfully updated")
            return redirect(reverse('profile'))
            
        else:
            messages.error(request, "Please only use alpha-numerics to complete address details")

    else:
        form = AddressForm()

    form = AddressForm()
    args = {'form':form}    
    return render(request, 'purchase/address.html', args)


@login_required() 
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

            user = get_object_or_404(User, username=request.user)

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


            messages.success(request, "Credit Card successfully updated")

            return redirect(reverse('profile'))


    else:
        today = datetime.date.today()
        form = CCRegistrationForm()
 
    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))
 
    return render(request, 'purchase/register_cc.html', args)
