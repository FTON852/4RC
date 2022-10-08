from django.contrib import admin
from .models import Account, Wallet, MonthlyPay

# Register your models here.
admin.site.register(Account)
admin.site.register(Wallet)
admin.site.register(MonthlyPay)
