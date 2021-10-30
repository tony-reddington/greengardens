from django.shortcuts import render


def index(request):
    """ View to retun home page """
    return render(request, 'home/index.html')
