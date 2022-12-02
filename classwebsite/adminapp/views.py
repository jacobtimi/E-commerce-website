from django.core.checks import messages
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from .forms import SignUpform, staff_form, User_form
from django.views import generic
from.forms import SignUpform, Product_form
from.models import Product_table, Profile
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpform
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def index_page(request):
    product_details = Product_table.objects.only('product_id', 'product_name', 'price', 'profile_picture').filter(status='approved')
    return render(request, 'index.html', {'product':product_details})


@login_required
def upload_product(request):
    if request.method == 'POST':
        form = Product_form(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.date_upload = timezone.now()
            post.status="unapprove"
            post.save()
            return HttpResponsePermanentRedirect(reverse('upload_prod'))
    else:
        form = Product_form()
        return render(request=request, template_name= 'adminapp/upload_product_form.html', context={'form':form})
       

@login_required
def manage_product(request):
    product_details = Product_table.objects.all()
    return render(request, 'adminapp/manage_product.html', {'product':product_details })     


@login_required
def approve_product(request, prod_id):
    products= Product_table.objects.get(product_id=prod_id)
    if products.status == "unapproved":
        products.status = "approved"
    else:
        products.status = "unapproved"
    products.save()
    return manage_product(request)


@login_required
def edit_product(request, prod_id):
    edit = get_object_or_404(Product_table, prod_id)
    form = Product_form (request.POST or None, request.FILES or None)
    return 0

@login_required
def delete_product(request, prod_id):
    pass


@login_required
def product_full_list(request, category):
    product_details = Product_table.objects.filter(category=category)
    return render(request=request, template_name='shop.html', context={"product":product_details})

@login_required
def product_description(request, prod_id):
    product_details = Product_table.objects.get(product_id=prod_id)
    return render(request=request, template_name='shop-single.html', context={"product":product_details})


@login_required
def manage_staff(request):
    staff_details = Profile.objects.all().filter(staff=True)
    return render(request, 'adminapp/manage_staff.html',{'staff':staff_details, 'status':'staff'})     

@login_required
def manage_customer(request):
    staff_details = Profile.objects.all().filter(staff=False)
    return render(request, 'adminapp/manage_staff.html',{'staff':staff_details, 'status':'customer'})     


@login_required
def staff_profile(request, user_id):
    customer_details= Profile.objects.all().filter(user_id = user_id)
    return render(request, 'adminapp/staff_profile.html',{'staff':customer_details, 'status':'customer'})

@login_required
def staff_profile(request, user_id):
    staff_details= Profile.objects.all().filter(user_id = user_id)
    return render(request, 'adminapp/staff_profile.html',{'staff':staff_details})


@login_required
@transaction.atomic
def edit_profile(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(request.POST, instance=user)
        profile_form= staff_form(request.POST or None, request. FILES or None, instance= user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            if profile_form.cleaned_data['staff']:
                user.is_staff = True
                user.save()
            else:
                user.is_staff =False
                user.save()
            messages.success(request, ('Your profile was successfully updated!'))
            staff_profile(request, user_id)
            return HttpResponsePermanentRedirect(reverse('edit_profile', args={user_id}))
        else:
            messages.error(request, ('please correct the error below!'))
            return HttpResponsePermanentRedirect(reverse('edit_profile', args={user_id}))
    else:
        user = get_object_or_404(User, id = user_id)
        user_form = User_form(instance=user)
        profile_form= staff_form(instance= user.profile)
        return render(request, 'adminapp/staff_update_form.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def staff_deactivate(request, user_id):
    staff = User.objects.get(id=user_id)
    if staff.is_activate:
        staff.is_active = False
    else:
        staff.is_active = True
    staff.save()
    return staff_profile(request, user_id)





