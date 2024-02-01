from django import forms
from .users_models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password', 'first_name', 'last_name', 'email']
