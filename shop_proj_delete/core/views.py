from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def get_index(request):
	return render(request, "index.html")

def get_contact(request):
	return render(request, "contact.html")

def get_services(request):
	return render(request, "services.html")

def get_profile(request):
    return render(request, 'profile.html')