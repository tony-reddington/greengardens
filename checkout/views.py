from django.shortcuts import render, redirect, reverse

import sweetify

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        sweetify.error(request, 'Ooops',
                       text="There's no items in your basket", icon='error')
        return redirect(reverse('home'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jk5DjEGAJ0QdMrrRPD8VlyYaYQXjxFkAzbCOIvuCYmlCxXAx1CNbbIBj6wWD7saHJUfCLZ8DRGkTnvagSy2Zsne00xfQ5wEMu',
    }

    return render(request, template, context)
