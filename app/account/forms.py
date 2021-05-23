from django import forms
from .models import User

class NewUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name','email','password', 'born_date','gender')
        