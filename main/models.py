from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from api.network import Core


class Wallet(models.Model):
    secret_key = models.CharField(max_length=100)
    public_key = models.CharField(max_length=100)


class Account(models.Model):
    CHOICES = {
        ('employee', 'employee'),
        ('admin', 'admin'),
        ('editor', 'editor'),
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    icon = models.ImageField(blank=True, default='icon.png')
    status = models.BooleanField(default=False)
    wallet = models.ForeignKey(Wallet, related_name='wallet', on_delete=models.CASCADE, blank=True, null=True)
    group = models.CharField(max_length=100, choices=CHOICES)

    def create_wallet(self):
        # wallet = Wallet(public_key="123", secret_key="321").save()

        network = Core()
        new_public, new_private = network.new_wallet()
        wallet = Wallet.objects.create(public_key=new_public, secret_key=new_private)
        self.wallet = wallet
        self.save()

    def get_absolute_url(self):
        return reverse('main:profile', kwargs={"pk": self.id})

    def __str__(self):
        return self.user.username


class MonthlyPay(models.Model):
    group = models.CharField(max_length=100)
    cost = models.FloatField()

    def __str__(self):
        return self.group + ' ' + str(self.cost)
