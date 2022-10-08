from django import forms


class TransferForm(forms.Form):
    money_count = forms.CharField(max_length=100)
