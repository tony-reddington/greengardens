from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import ProfileForm

import sweetify

def profile(request):
    """ View to display the users profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Updated',
                     text="Your address has been updated",
                     icon='success')

    form = ProfileForm(instance=profile)
    user_orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'user_orders': user_orders,
    }
    return render(request, template, context)
