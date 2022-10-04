from email.policy import default
from django.db import models


class ProductCard(models.Model):
    name = models.CharField(max_length=200)
    alt = models.CharField(max_length=50, blank=True)
    image_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductPage(models.Model):
    product = models.ForeignKey(
        ProductCard, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50, blank=True)
    alt = models.CharField(max_length=50, blank=True)
    image_url = models.CharField(max_length=200)
    active = models.BooleanField(
        default=False, help_text="Active means this image will display first in carousel")

    def __str__(self):
        return self.title
