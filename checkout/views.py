from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings

import sweetify
import stripe

from bag.contexts import bag_products
from .models import Order, OrderLineItem
from products.models import Product
from .forms import OrderForm


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email_address': request.POST['email_address'],
            'telephone_number': request.POST['telephone_number'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'city_or_town': request.POST['city_or_town'],
            'county_or_state': request.POST['county_or_state'],
            'postcode_or_zip': request.POST['postcode_or_zip'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    sweetify.error(request, title='Sorry',
                                   text='One of the items in your basket was not found',
                                   icon='error')
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            sweetify.error(request, title='Sorry',
                           text='There was error while submitting your form',
                           icon='error')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            sweetify.error(request, 'Sorry',
                           text="There's no items in your basket",
                           icon='error')
            return redirect(reverse('home'))

        current_bag = bag_products(request)
        total = current_bag['grand_total']

        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """ View to handle successful checkouts """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    sweetify.success(request, 'Order Successful',
                     text="A confirmation email will be sent to your email address ",
                     icon='success', timer=3000, timerProgressBar='true')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)