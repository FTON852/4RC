from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Wallet(models.Model):
    secret_key = models.CharField(max_length=100)
    public_key = models.CharField(max_length=100)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    icon = models.ImageField(blank=True, default='icon.jpg')
    status = models.BooleanField()
    wallet = models.ForeignKey(Wallet, related_name='wallet', on_delete=models.CASCADE)
    group = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('main:profile', kwargs={"pk": self.id})
    def __str__(self):
        return self.user.username

class MonthlyPay(models.Model):
    group = models.CharField(max_length=100)
    cost = models.FloatField()

    def __str__(self):
        return self.group + ' ' + str(self.cost)