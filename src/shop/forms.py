from django import forms


class CheckoutForm(forms.Form):
    phone_number = forms.CharField(max_length=15)
    amount = forms.FloatField(min_value=0.01)
