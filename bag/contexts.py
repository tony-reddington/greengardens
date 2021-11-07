from decimal import Decimal
from django.conf import settings

def bag_products(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.QUALIFY_FOR_FREE_DELIVERY & total > 0:
        delivery = total + Decimal(settings.STANDARD_DELIVERY)
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