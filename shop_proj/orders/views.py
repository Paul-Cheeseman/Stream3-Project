from __future__ import unicode_literals
from django.shortcuts import render
from products.models import Product
from accounts.models import User
from orders.models import Order, OrderItem
from django.contrib import messages



# Create your views here.
def orders_list(request):

	#identify customer
	customer = User.objects.get(username=request.user)
	
	#identify specific order ids for customer
	customer_specific_order_ids = OrderItem.objects.filter(customer_id=customer).values('order_id').distinct()

	#Timmy Help
	global orders_dict
	orders_dict = {}

	#Process order items into customer specific order gorupings
	for item in customer_specific_order_ids:
		#Generate query set of order items for given order id 
		order = OrderItem.objects.filter(order_id = item['order_id'])
		#Put query item into a dictionary which can be passed to template
		orders_dict.update({item['order_id']:order})


	# Loop through the order groupings to give access to each order group
	for key, order in orders_dict.items():
		#For each order group, iterate through for invidual items and change product_id to product_name
		for order_item in order:
			order_item.product_id = (Product.objects.get(id=order_item.product_id))
			#print("order date")
			#print(order_item.order_date)
			
	
	return render(request, "orders/orders.html", {"orders_dict": orders_dict})