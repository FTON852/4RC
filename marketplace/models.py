from autoslug import AutoSlugField
from django.db import models


# Create your models here.
from django.urls import reverse

from main.models import Account


class Item(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(max_length=255, verbose_name='url', unique=True, populate_from='title')
    price = models.FloatField(default=0.0)
    description = models.TextField(max_length=2000)
    image = models.ImageField(default="default.png")
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('core:product', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
