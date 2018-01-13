from django import template
from cart.models import Cart

register = template.Library()

#A template tag to show the about of items in a cart on the badge icon
#placed next to the cart link on the menu
@register.simple_tag(takes_context=True)
def cart_item_amount(context):
    request = context['request']

    if 'cart' in request.session:
        cart_num = request.session['cart']
        cart = Cart.get_cart(cart_num)
        return cart.amount_items_in_cart()
    else:
        return 0
