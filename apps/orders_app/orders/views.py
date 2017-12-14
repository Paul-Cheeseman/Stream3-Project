from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from products.models import Product
from accounts.models import User
from orders.models import Order, OrderItem
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum, F



# Create your views here.
def orders_list(request):

	#identify customer
	customer = get_object_or_404(User, username=request.user)
	
	all_customer_orders = Order.objects.filter(customer_id=customer)

	#for each customer order, pull out the all the order items
	all_customer_items = OrderItem.objects.filter(order_id__in=all_customer_orders)

	###########################################################
	#Need to get the date from the order object for each orderitem!!!!!!!!!!!!!!
	###########################################################

	for item in all_customer_items:
		print("Item Quant")
		print (item.quantity)
		item.date = Order.objects.get(id = item.order_id).order_date
		item.total = item.price * item.quantity
		#item.order_total = Order.objects.get(id = item.order_id).order_date		
		print("Date")
		print(item.date)
	
	all_customer_items

	page = request.GET.get('page', 1)

	#Paginate the customer orders to 15 per page (should cater for very big orders)
	paginator = Paginator(all_customer_items, 15)

	try:
		customer_orders = paginator.page(page)
	except PageNotAnInteger:
		customer_orders = paginator.page(1)
	except EmptyPage:
		customer_orders = paginator.page(paginator.num_pages)
	
	return render(request, "orders/Orders.html", {"customer_orders": customer_orders})
