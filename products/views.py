from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ View to return all products with sorting and searching capabilities """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """ View to return information about a specific product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)
