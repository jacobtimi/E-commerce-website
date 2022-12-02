from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Product_table(models.Model):
    cat = (
        ("wears", "wears"),
        ("watch", "watch"),
        ("Electronics", "Electronics"),
        ("Shoes", "Shoes")
    )

    d_type = (
        ("Featured product", "Featured product"),
        ("Category product", "Category product"),
        ("None", "None")
    )


    product_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(unique=True, max_length=50)
    date_upload = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(unique=False)
    price = models.IntegerField(unique=False)
    description = models.CharField(unique=False, max_length=100, null=True)
    profile_picture = models.ImageField(upload_to='product_image', unique=True)
    status = models.CharField(unique=False, max_length=10, null=True)
    category = models.CharField(max_length=20, choices=cat, default=None)
    display_type = models.CharField(unique=False, max_length=20, choices= d_type, default=None)


class Profile(models.Model):
    countries = [
        ("Nigeria", "Nigeria"),
        ("Ghana", "Ghana"),
        ("United kingdom", "United kingdom"),
        ("USA", "USA")
    ]
    states = [
                ("Abia", "Abia"),
                ("Oyo", "Oyo"),
                ("Osun", "Osun"),
                ("Lagos", "Lagos"),
                ("Kano", "Kano"),
                ("Abuja", "Abuja"),
    ]

    position = [
        ("CEO", "CEO"),
        ("GMD", "GMD"),
        ("CTO", "CTO"),
        ("Supervisor", "Supervisor"),
        ("Accountant", "Accountant"),
        ("Marketer", "Marketer"),
        ("Staff", "Staff"),
        ("HR", "HR"),
    ]

    ma_status = [
        ("single",  "single"),
        ("married",  "married"),
        ("Divorced",  "Divorced"),
        ("complicated",  "complicated")
    ]

    user  =  models.OneToOneField(User, on_delete=models.CASCADE )
    status= models.CharField(unique=False, max_length=100, null=True)
    address= models.CharField(unique=False, max_length=100, null=True)
    phone_number = models.CharField(unique = True, max_length=100, null=True)
    nationality= models.CharField(choices=countries, unique=False, max_length=20, null=True)
    state= models.CharField(choices=states, unique=False, max_length=20, null=True)
    means_of_identity= models.ImageField(upload_to='identityImage/', unique=False, null=True)
    particulars= models.FileField(upload_to='particularImage/', unique=False, null=True)
    profile_passport= models.ImageField(upload_to='staffImage/', unique=False, null=True)
    position= models.CharField(choices=position, unique=False, max_length=20, null=True)
    marital_status=models.CharField(choices=ma_status, unique=False, max_length=12, null=True)
    staff = models.BooleanField(default=False, unique=False)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
