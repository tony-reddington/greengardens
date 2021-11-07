from django.shortcuts import render, redirect


def view_bag(request):
    """ View to return bag contents """
    return render(request, 'bag/bag.html')

def add_product_to_bag(request, item_id):
    """ Add a quantity of selected product to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    user_bag = request.session.get('bag', {})

    if item_id in list(user_bag.keys()):
        user_bag[item_id] += quantity
    else:
        user_bag[item_id] = quantity

    request.session['bag'] = user_bag
    return redirect(redirect_url)
