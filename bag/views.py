from django.shortcuts import (
    render, redirect, get_object_or_404, reverse, HttpResponse)

from products.models import Product

import sweetify


def view_bag(request):
    """ View to return bag contents """
    return render(request, 'bag/bag.html')


def add_product_to_bag(request, item_id):
    """ Adds a quantity of a selected product to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    user_bag = request.session.get('bag', {})

    if item_id in list(user_bag.keys()):
        user_bag[item_id] += quantity
    else:
        user_bag[item_id] = quantity
    sweetify.success(request, 'Done!',
                     text='Product added to your basket', icon='success')

    request.session['bag'] = user_bag
    return redirect(redirect_url)


def update_bag_quantity(request, item_id):
    """ Updates product quantity in bag """

    get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    user_bag = request.session.get('bag', {})
    if quantity > 0:
        user_bag[item_id] = quantity
    else:
        user_bag.pop(item_id)
    sweetify.success(request, 'Updated',
                     text='The quantity has been updated', icon='success')

    request.session['bag'] = user_bag
    return redirect(reverse('view_bag'))


def delete_bag_product(request, item_id):
    """ Delete product from the bag """

    get_object_or_404(Product, pk=item_id)
    user_bag = request.session.get('bag', {})
    user_bag.pop(item_id)
    sweetify.success(request, 'Removed',
                     text='The product has been removed', icon='info')

    request.session['bag'] = user_bag
    return redirect(reverse('view_bag'))
