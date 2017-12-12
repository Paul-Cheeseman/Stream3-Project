from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from products.models import Product
from accounts.models import User
from orders.models import Order, OrderItem
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def orders_list(request):

	#identify customer
	customer = get_object_or_404(User, username=request.user)
	
	all_customer_orders = OrderItem.objects.filter(customer_id=customer)
	print("All customer orders")
	for item in all_customer_orders:
		item.product = get_object_or_404(Product, id=item.product_id)



	page = request.GET.get('page', 1)

	#Paginate the customer orders to 15 per page (should cater for very big orders)
	paginator = Paginator(all_customer_orders, 15)

	try:
		customer_orders = paginator.page(page)
	except PageNotAnInteger:
		customer_orders = paginator.page(1)
	except EmptyPage:
		customer_orders = paginator.page(paginator.num_pages)
	
	return render(request, "orders/orders.html", {"customer_orders": customer_orders})