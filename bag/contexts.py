from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_products(request):

    bag_items = []
    total = 0
    product_count = 0
    user_bag = request.session.get('bag', {})

    for item_id, quantity in user_bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.QUALIFY_FOR_FREE_DELIVERY:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENT / 100)
        if delivery < 5 and delivery > 0:
            delivery = 5
        spend_for_free_delivery = settings.QUALIFY_FOR_FREE_DELIVERY - total
    else:
        delivery = 0
        spend_for_free_delivery = 0


    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'qualify_for_free_delivery': settings.QUALIFY_FOR_FREE_DELIVERY,
        'spend_for_free_delivery': spend_for_free_delivery,
        'grand_total': grand_total
    }

    return context