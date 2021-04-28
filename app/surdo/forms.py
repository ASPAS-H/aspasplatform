from django import forms
from .models import Deaf

class NewDeafForm(forms.ModelForm):

    class Meta:
        model = Deaf
        fields = ('name', 'phone', 'cpf', 'health_plan')
        