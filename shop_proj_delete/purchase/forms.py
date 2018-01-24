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
 

    #stripe checks/validates the info and user is restricted by above for other input, plus it is 
    #apparent what is required, so not adding validation tests
    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    def save(self, stripe_token, user, commit=True):
        #update user with credit card stripe token to enable re-use
        user.stripe_id = stripe_token
        user.save()



class AddressForm(forms.Form):
    alpha = RegexValidator(r'^[A-Za-z ]*$')
    alpha_num = RegexValidator(r'^[A-Za-z0-9 ]*$')    
    address_line1 = forms.CharField(validators=[alpha_num])
    address_line2 = forms.CharField(validators=[alpha_num])
    county = forms.CharField(validators=[alpha])
    postcode = forms.CharField(validators=[alpha_num])


    def clean_postcode(self):
        postcode = self.cleaned_data.get('postcode')
        if len(postcode) < 7 or len(postcode) > 8:
            message = "Please enter a valid postcode"
            raise forms.ValidationError(message)
 
        return postcode

