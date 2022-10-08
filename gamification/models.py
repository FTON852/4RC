from django.db import models

from main.models import Account


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    reward = models.FloatField()


class Achievements(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    achieve = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
