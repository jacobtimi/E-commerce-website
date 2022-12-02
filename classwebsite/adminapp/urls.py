from django.conf.urls import url
from classwebsite.adminapp import views as admin_view

# urlpatterns= [
#      url(r'^product_upload/', admin_view.upload_product, name= 'upload_prod'),
#      url(r'^product_description/(?P<user_id>\d+)/', admin_view.addToCart, name= 'prod_description'),
#      url(r'^manage_product/', admin_view.manage_product, name= 'manage_prod'),
#      url(r'^manage_staff/', admin_view.manage_staff, name= 'manage_staff'),
#      url(r'^staff_profile/(?P<user_id>\d+)/', admin_view.staff_profile, name= 'staff_profile'),
#      url(r'^user_profile/(?P<user_id>\d+)/', admin_view.manage_product, name= 'user_profile'),
#      url(r'^product_status/(?P<prod_id>\d+)/', admin_view.approve_product, name= 'status_prod'),
#      url(r'^edit_product/(?P<prod_id>\d+)/', admin_view.edit_product, name= 'edit_prod'),
#      url(r'^delete_product/(?P<user_id>\d+)/', admin_view.delete_product, name= 'delete_prod'),    
#      url(r'^product_list/(?P<category>\D+)/', admin_view.product_full_list, name= 'list_prod'),    
# ]

urlpatterns = [
    url(r'^product_upload/', admin_view.upload_product, name='upload_prod'),
    url(r'^manage_upload/$', admin_view.manage_product, name='manage_prod'),
    url(r'^user_profile/(?P<user_id>\d+)/', admin_view.manage_product, name='user_profile'),
    url(r'^product_status/(?P<prod_id>\d+)/', admin_view.approve_product,name='status_prod'),
    url(r'^edit_product/(?P<prod_id>\d+)/', admin_view.edit_product, name='edit_prod'),
    url(r'^edit_profile/(?P<user_id>\d+)/', admin_view.edit_profile, name='edit_profile'),
    url(r'^delete_product/(?P<prod_id>\d+)/', admin_view.delete_product, name='delete_prod'),
    url(r'^product_list/(?P<category>\D+)/', admin_view.product_full_list, name='list_prod'),
    # url(r'^product_list/(?P<featured>\D+)/', admin_view.product_full_list, name='list_prod'),
    url(r'^manage_staff/$', admin_view.manage_staff, name='manage_staff'),
    url(r'^manage_customer/$', admin_view.manage_customer, name='manage_customer'),
    url(r'^staff_profile/(?P<user_id>\d+)/', admin_view.staff_profile, name='staff_profile'),
    url(r'^staff_deactivate/(?P<user_id>\d+)/', admin_view.staff_deactivate, name='staff_deactivate'),
]    
