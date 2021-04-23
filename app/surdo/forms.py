from django import forms
from .models import Deaf

class NewDeafForm(forms.ModelForm):

    class Meta:
        model = Deaf
        fields = ('name', 'born_date', 'email', 'password', 'address', 'phone', 'cpf', 'health_plan')
        