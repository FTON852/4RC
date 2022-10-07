from django import forms

class WithdrawForm(forms.Form):
    money_count = forms.CharField(max_length=100)