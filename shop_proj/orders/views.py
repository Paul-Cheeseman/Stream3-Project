from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from products.models import Product
from accounts.models import User
from orders.models import Order, OrderItem
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum, F
from datetime import datetime
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def orders_list(request):

	#identify customer
	customer = get_object_or_404(User, username=request.user)
	
	#get all customer orders
	order_list = Order.objects.filter(customer_id=customer)

	#Switch order so most recent appears first on page
	order_list = order_list.order_by('-id')


	if not order_list.exists():
		messages.info(request, "You currently have no orders to view")          

	else:
		#Run through each of the customers orders and put in an individual time and date field from timedate stamp
		for order in order_list:
			order.date = order.order_date.date()
			order.time = order.order_date.time().strftime('%H:%M:%S')
		
			#For each order, go through the associated order items and retrieve the quantities orders so can 
			#publish the deliver amount
			order_items = OrderItem.objects.filter(order_id=order.id)
			item_quantity = 0
			for item in order_items:
				item_quantity = item_quantity + item.quantity
			#The *2 is for the £2 delivery charge, ideally this would be a global var that would be referenced
			order.total = order.total + (item_quantity * 2)

	#Paginating output (if required)
	page = request.GET.get('page', 1)

	#Paginate the orders to 2 per page
	paginator = Paginator(order_list, 3)

	try:
		customer_orders = paginator.page(page)
	except PageNotAnInteger:
		customer_orders = paginator.page(1)
	except EmptyPage:
		customer_orders = paginator.page(paginator.num_pages)

	return render(request, "orders/list.html", {"customer_orders": customer_orders})



@login_required()
def orders_detail(request):

	order = 0
	order_id = 0

	if request.GET.get('id'):
	
		order_id = request.GET.get('id')

		#order items
		order = OrderItem.objects.filter(order_id=order_id)

		overall_total = 0
		delivery_cost = 0
		complete_total = 0
		overall_quantity = 0

		for item in order:
			product = get_object_or_404(Product, id=item.product_id)
			item.total = item.quantity * product.price
			item.name = product.name
			item.description = product.description
			overall_quantity = overall_quantity + item.quantity
			overall_total = overall_total + item.total

		#£2 deliver charge per item
		delivery_cost = overall_quantity * 2
		complete_total = overall_total + delivery_cost


	return render(request, "orders/detail.html", {"order": order, "overall_total": overall_total, "delivery_cost": delivery_cost, "complete_total": complete_total, "order_id": order_id})


