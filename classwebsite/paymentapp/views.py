from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from classwebsite.adminapp.models import Product_table
from .models import Order_table, Invoice_table
from django.utils import timezone
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .form import AddToCart_form, PaymentOption_form, CardDetails_form
from django.db import transaction

price = 0
@login_required
def addToCart(request, prod_id):
    global price
    if request.method == 'POST':
        form = AddToCart_form(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data["quantity"]
            total_price = int(quantity) * int(price)
        post = Order_table(price=total_price, quantity=quantity)
        post.user_id  = request.user.id
        post.date_upload = timezone.now()
        post.product.id = prod_id
        post.save()
        return HttpResponsePermanentRedirect(reverse('cart_prod'))
    else:
        form = AddToCart_form()
        product_details  = Product_table.objects.get(product_id=prod_id)
        price =  product_details.price
        content = {'form':form, "product":product_details}
        return render(request=request, template_name='shop-single.html',context={'form':form ,'product':product_details})



# price =0
# @login_required
# def addToCart(request, prod_id):
#     global price
#     if request.method == "POST":
#         form =AddToCart_form(request.POST)
#         if form.is_valid():
#             quantity = form.cleaned_data["quantity"]
#             total_price = int(quantity) * int(price)
#         post = Order_table(price =total_price, quantity =quantity)
#         post.user_id =request.user.id
#         post.data_upload =timezone.now()
#         post.product_id = prod_id
#         post.save()
#         return HttpResponsePermanentRedirect(reverse('cart_prod'))
    
#     else:
#         form =AddToCart_form()
#         product_details = Product_table.objects.get(product_id =prod_id)
#         price =product_details.price
#         content = {'form':form, "product":product_details}
#         return render(request=request, template_name='shop-single.html',context={'form':form ,'product':product_details})



# def product_FromCart(request):
#     cart_details = Order_table.objects.filter(user_id=request.user.id)
#     return render(request, 'paymentapp/cart_prooduct.html', {'product':cart_details})

@login_required
def product_FromCart(request, prod_id):
    cart_details = Order_table.objects.filter(user_id = request.user.id, purchased=False)
    return render(request, "paymentapp/cart_product.html", {'product': cart_details})


@login_required
def edit_Order(request, prod_id):
    global price
    edit = get_object_or_404(Order_table, product_id=prod_id)
    form = AddToCart_form(request.POST or None, request.FILES or None, instance=edit)
    if request.method == 'POST':
        if(form.is_valid):
            form.save()
            details = Order_table.objects.get(product_id=prod_id)
            price = int(details.quantity) * int(price)
            Order_table.objects.filter(product_id=prod_id).update(price=price)
            return product_FromCart(request)
    product_details = Product_table.objects.get(product_id=prod_id)
    price = product_details.price
    template_name = "shop-single.html"        
    return render(request, template_name, context = {'form':form, "product":product_details})


@login_required
def delete_Order(request, order_id):
    Order_table.objects.filter(order_id = order_id).delete()
    return product_FromCart(request)
    
    
@login_required
def order_Receipt(request, user_id):
    price = 0
    order =Order_table.objects.filter(user_id =user_id)
    for value in order.values():
        price +=int(value['price'])
    receipt = Invoice_table(date_cashout=timezone.now(), user_id = user_id, total_price=price)
    receipt.save()
    receipt_details =Invoice_table.objects.filter(user_id =user_id, cashout=False)
    return render(request, template_name = "paymentapp/receipt.html", context ={"receipt": receipt_details.values()[0], 'order':order})


@login_required
def payment_service(request, user_id):
    form = PaymentOption_form(request.POST)
    if request.method == 'POST':
        if form.is_valid ():
            option = form.cleaned_data['option']       
        if  option == 'pay_delivery':
            receipt_details = Invoice_table.objects.filter(user_id=user_id, cashout=False)
            return render(request, template_name = "paymentapp/success_pay.html", context ={"receipt":receipt_details.values()[0]})
        else:
           return HttpResponsePermanentRedirect(reverse('cart_detail', args=(user_id)))

    else:
        form = PaymentOption_form()       
        return render(request, template_name ="paymentapp/payment_service.html", context ={"form":form})
        receipt = Invoice_table(date_cashout = timezone.now, user_id = user_id,
        cashout=False)
        return render(request, template_name = "paymentapp/payment_service.html",  context ={"receipt":receipt_details.values()[0]})


@transaction.atomic
@login_required
def card_detail(request, user_id):
    form = PaymentOption_form(request.POST)
    if request.method == 'POST':
        if (form.is_valid):
            card_number = form.cleaned_data['card_number']
            card_cvv = form.cleaned_data['card_cvv']
            cardExpiry_date = form.cleaned_data['card_expiry_date']
            
            option = form.cleaned_data['option']
        order = Order_table.objects.filter(user_id= user_id, purchased=False)
        order.purchased= True
        invoice = Invoice_table.objects.filter(user_id=user_id,cashout=True )

        if option == 'pay_delivery':
            receipt_details =Invoice_table.objects.filter(user_id=user_id, cashout=False)
            return render(request, template_name="paymentapp/sucess_pay.html",context={"receipt":receipt_details.values()[0]})
        else:
            return HttpResponsePermanentRedirect(reverse('card_detail', args=(user_id)))

    else:
        form= PaymentOption_form()
        return render(request, template_name='paymentapp/payment_service.html', context={"form":form})
           

 

@login_required
def cancel_order(request,user_id):
    Invoice_table.objects.filter(user_id=user_id, cashout=False).delete()
    return product_FromCart(request)

@transaction.atomic  
@login_required
def card_detail(request, user_id):
    form = CardDetails_form(request.POST)
    if request.method == 'POST':
        if(form.is_valid):
            cardName = form.cleaned_data['card_name']    
            cardNumber = form.cleaned_data['card_number']    
            cardCvv = form.cleaned_data['card_cvv']       
            cardExpiryDate = form.cleaned_data['card_expiry_date']  
        order =Order_table.objects.filter(user_id=user_id,purchased=False).update(purchased=True)
        order.save()
        invoice =Invoice_table.objects.filter(user_id=user_id,cashout=False).update(cashout=True) 
        return render(request, template_name ="paymentapp/success_pay.html", context ={"form":form})      
      
    else:
        form = CardDetails_form()
        return render(request, template_name = "paymentapp/card_detail.html",context={"from":form})
   
