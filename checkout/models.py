import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=50, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.EmailField(max_length=250, null=False, blank=False)
    telephone_number = models.CharField(max_length=20, null=False, blank=False)
    address_line1 = models.CharField(max_length=100, null=False, blank=False)
    address_line2 = models.CharField(max_length=100, null=True, blank=True)
    city_or_town = models.CharField(max_length=50, null=False, blank=False)
    county_or_state = models.CharField(max_length=50, null=True, blank=True)
    postcode_or_zip = models.CharField(max_length=15, null=True, blank=True)
    country = CountryField(max_length=50, null=False, blank=False)
    date_of_order = models.DateTimeField(auto_now_add=True)
    total_order = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _order_number_generation(self):
        """ Generate a random order number """
        return uuid.uuid4().hex.upper()


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank-False, default=0)
    line_item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
