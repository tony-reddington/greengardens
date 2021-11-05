from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Subcategory


def all_products(request):
    """ View to return all products with sorting and searching capabilities """

    products = Product.objects.all()
    query = None
    sub_categories = None

    if request.GET:
        if 'sub' in request.GET:
            sub_categories = request.GET['sub'].split(',')
            products = products.filter(sub__name__in=sub_categories)
            sub_categories = Subcategory.objects.filter(name__in=sub_categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'No search criteria has been entered.')
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(details__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_text': query,
        'current_subcategories': sub_categories,
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """ View to return information about a specific product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)
