# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm, CCRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm, UserLoginForm
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
 
            if user:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))
 
            else:
                messages.error(request, "unable to log you in at this time!")
 
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
        form = CCRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            #print data['stripe_id']
            #print request.user.email
            #print data['stripe_id']
            form.save(data['stripe_id'], request.user)

    #The form on intial page load (blank)
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