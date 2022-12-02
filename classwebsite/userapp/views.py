from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from classwebsite.adminapp.models import Profile
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User
from. form import Customer_form
from classwebsite.adminapp.forms import User_form
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

# Create your views here.
@login_required
def customer_profile(request, user_id):
    customer_details= Profile.objects.all().filter(user_id = user_id)
    return render(request, 'userapp/customer_profile.html',{'customer':customer_details, 'status':'customer'})

@login_required
def edit_customer(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(request.POST, instance=user)
        profile_form= Customer_form(request.POST or None, request. FILES or None, instance= user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponsePermanentRedirect(reverse('customer_profile', args={user_id}))
        else:
            messages.error(request, ('please correct the error below!'))
            return HttpResponsePermanentRedirect(reverse('edit_customer', args={user_id}))
    else:
        user = get_object_or_404(User, id = user_id)
        user_form = User_form(instance=user)
        profile_form= Customer_form(instance= user.profile)
        return render(request, 'userapp/customer_update_form.html', {'user_form': user_form, 'profile_form': profile_form})
