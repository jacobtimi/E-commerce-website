from django.conf.urls import url
from classwebsite.userapp import views as user_view


urlpatterns = [
    url(r'^edit_customer/(?P<user_id>\d+)/', user_view.edit_customer, name='edit_customer'),
    url(r'^customer_profile/(?P<user_id>\d+)/', user_view.customer_profile,name='customer_profile'),
    
]