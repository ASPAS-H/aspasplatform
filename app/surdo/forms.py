from django import forms
from .models import Deaf, Consult

class NewDeafForm(forms.ModelForm):

    class Meta:
        model = Deaf
        fields = ('phone', 'cpf', 'health_plan')

class ConsultForm(forms.ModelForm):

    class Meta:
        model = Consult
        fields = ('date1', 'date2', 'date3', 'observations', 'modelity')
        