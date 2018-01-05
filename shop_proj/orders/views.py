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
	order_list = Order.objects.filter(customer_id=customer)
	

	for order in order_list:
		order.date = order.order_date.date()
		order.time = order.order_date.time().strftime('%H:%M:%S')

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

	return render(request, "orders/detail.html", {"customer_orders": customer_orders})



@login_required()
def orders_detail(request):
	
	if request.GET.get('id'):
	
		#order items
		order = OrderItem.objects.filter(order_id=request.GET.get('id'))

		overall_total = 0

		for item in order:
			item.product = get_object_or_404(Product, id=item.product_id)
			item.total = item.quantity * item.price
			overall_total = overall_total + item.total

	return render(request, "orders/detail.html", {"order": order, "overall_total": overall_total})


