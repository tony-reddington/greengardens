from django.shortcuts import render


def profile(request):
    """ View to display the users profiles """
    template = 'profiles/profile.html'
    context = {

    }
    return render(request, template, context)
