from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('line_item_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    
    readonly_fields = ('order_number', 'date_of_order',
                       'delivery_cost', 'total_order',
                       'grand_total',)

    list_display = ('order_number', 'date_of_order', 'full_name',
                    'total_order', 'delivery_cost', 'grand_total',)

    ordering = ('-date_of_order',)

admin.site.register(Order, OrderAdmin)
