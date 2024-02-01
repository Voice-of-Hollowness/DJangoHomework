from django import forms
from .banks_models import Bank

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['bank_name', 'routing_number', 'swift_bic']
