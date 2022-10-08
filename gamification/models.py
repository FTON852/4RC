from django.db import models

from main.models import Account


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    reward = models.FloatField()

    def __str__(self):
        return f'{self.title} {self.reward}'


class Achievements(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    achieve = models.ForeignKey(Achievement, on_delete=models.CASCADE, unique=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.user.username} {self.achieve.title} {self.status}'
