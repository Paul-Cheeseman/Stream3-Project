from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from products.models import Product
from accounts.models import User
from orders.models import Order, OrderItem
from django.contrib import messages



# Create your views here.
def orders_list(request):

	#identify customer
	customer = get_object_or_404(User, username=request.user)
	
	all_customer_orders = OrderItem.objects.filter(customer_id=customer)
	print("All customer orders")
	for item in all_customer_orders:
		item.product = get_object_or_404(Product, id=item.product_id)

	return render(request, "orders/orders.html", {"all_customer_orders": all_customer_orders})