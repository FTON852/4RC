from autoslug import AutoSlugField
from django.db import models

# Create your models here.
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(max_length=255, verbose_name='url', unique=True, populate_from='title')
    description = models.TextField(max_length=2000)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default="default.png")
    reward = models.FloatField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_feed:event', kwargs={"slug": self.slug})
