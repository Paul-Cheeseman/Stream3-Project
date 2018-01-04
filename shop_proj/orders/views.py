from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from products.models import Product
from accounts.models import User
from orders.models import Order, OrderItem
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum, F
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def orders_list(request):

	#identify customer
	customer = get_object_or_404(User, username=request.user)
	
	#get all customer orders
	orders = Order.objects.filter(customer_id=customer)
	
	groups = {}




	# Create a new data structure that maps date/day to
	# all the orders for this user on that particular
	# day as well as a running total 
	for order in orders:

		if order.day not in groups:
		# Create the initial entry for this day
			groups[order.day] = {
				"total": 0,
				"daily_orders": {"OrderID": order.id, "OrderItems": []}
			}

		if order.day in groups:
			#print("order.day")
			#print(order.day)


			
			############This is being overwritten, not creating a new OrderID entry


			#for each cart item, use the stored order_id to retrive orderItem from orderItem table
			order_items = OrderItem.objects.filter(order_id=order.id)

			for order_item in order_items:
				groups[order.day]["daily_orders"]["OrderID"] = order.id
				groups[order.day]["daily_orders"]["OrderItems"].append(order_item)
			
			# Add the prices for all order items to total
			for item in orders:
				groups[order.day]["total"] += item.total



	print("Groups")
	print(groups)


	#Paginate the customer orders to 15 per page (should cater for very big orders)
	#paginator = Paginator(all_customer_items, 15)
	#try:
	#	customer_orders = paginator.page(page)
	#except PageNotAnInteger:
	#	customer_orders = paginator.page(1)
	#except EmptyPage:
	#	customer_orders = paginator.page(paginator.num_pages)

	return render(request, "orders/orders.html", {"groups": groups})









	
	
	