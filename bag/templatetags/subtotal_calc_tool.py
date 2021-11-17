# Calculates the subtotal price multiplying the price by the quantity
from django import template

register = template.Library()


@register.filter(name='subtotal_calc')
def subtotal_calc(price, quantity):
    return price * quantity
