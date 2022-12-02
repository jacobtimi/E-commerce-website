from  django import  forms
from django.contrib.auth.models import User
from django.apps import AppConfig
from django.forms import widgets
from. models import Order_table



class AddToCart_form(forms.ModelForm):
    class Meta:
        model = Order_table
        fields = [
            'quantity',
        ]   

class PaymentOption_form(forms.Form):
    CHOICES = [('master_card', 'Master_card'),
                ('visa_card', 'visa card'),
                ('pay_delivery', 'pay_delivery'),
    ]
    option = forms.ChoiceField(choices=CHOICES, widget= forms.RadioSelect)

class CardDetails_form(forms.Form):
    card_name = forms.CharField(max_length=20, help_text= 'Enter your card name')
    card_number = forms.CharField(max_length=16, help_text= 'Enter your card number')
    card_cvv = forms.CharField(max_length=3, help_text= 'Enter your card cvv')
    card_expiry_date = forms.CharField(max_length=10, help_text= 'Enter your card expiry number')