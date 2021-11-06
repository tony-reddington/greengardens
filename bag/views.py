from django.shortcuts import render


def view_bag(request):
    """ View to return bag contents """
    return render(request, 'bag/bag.html')