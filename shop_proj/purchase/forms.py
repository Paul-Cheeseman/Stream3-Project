from django import forms
from accounts.models import User
from django.core.exceptions import ValidationError 
from django.core.validators import RegexValidator, EmailValidator




class CCRegistrationForm(forms.Form):
    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]
    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in range(2018, 2036)]
 
    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
 

    def save(self, stripe_token, user, commit=True):
        #update user with credit card, generate stripe token at checkout
        user.stripe_id = stripe_token
        user.save()





class AddressForm(forms.Form):
    alpha_num = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only use alpha-numeric characters for address information.')
    address_line1 = forms.CharField(validators=[alpha_num])
    address_line2 = forms.CharField(validators=[alpha_num])
    county = forms.CharField(validators=[alpha_num])
    postcode = forms.CharField(validators=[alpha_num])
