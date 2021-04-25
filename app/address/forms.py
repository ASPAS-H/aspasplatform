from django import forms
from .models import Address

class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('street', 'vile', 'state', 'zipCode', 'complement', 'city')
        