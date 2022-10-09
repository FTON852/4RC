from django import forms
from .models import Account


class TransferForm(forms.Form):
    money_count = forms.CharField(max_length=100)


class AccountCreateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['user', 'group']
