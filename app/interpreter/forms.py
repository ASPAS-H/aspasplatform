from django import forms
from .models import Interpreter

class NewInterpreter(forms.ModelForm):

    class Meta:
        model = Interpreter
        fields = ('phone','cpf','librasFluence')