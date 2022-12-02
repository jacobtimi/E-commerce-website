from django.apps import AppConfig
from django.conf.urls import url
from classwebsite.paymentapp import views as payment_view


urlpatterns =[
    url(r'^product_description/(?P<prod_id>\d+)/', payment_view.addToCart, name='user_profile'),    
    url(r'^cart_product/', payment_view.product_FromCart, name = 'cart_prod'),
    url(r'^product_description/(?P<prod_id>\d+)/', payment_view.edit_Order, name='order_edit'),    
    url(r'^delete_order/(?P<prod_id>\d+)/', payment_view.delete_Order, name = 'order_del'),
    url(r'^order_receipt/(?P<user_id>\d+)/', payment_view.order_Receipt, name = 'receipt'),
    url(r'^pay_service/(?P<user_id>\d+)/', payment_view.payment_service, name = 'pay_service'),
    url(r'^cancel_order/(?P<user_id>\d+)/', payment_view.cancel_order, name = 'cancel_order'),
    url(r'^card_detail/(?P<user_id>\d+)/', payment_view.card_detail, name = 'card_detail'),  
]
