from email import message
from os import replace
from random import choices
from django.utils.translation import gettext_lazy as _

from django.db import models


class ProductCard(models.Model):
    name = models.CharField(max_length=200)
    alt = models.CharField(max_length=50, blank=True)
    image_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    @property
    def object_id(self):
        value = self.name
        return '%s_%s' % (value.replace(" ", ""), self.id)

    def __str__(self):
        return self.name


class ProductPage(models.Model):
    product = models.ForeignKey(
        ProductCard, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50, default="No description")
    alt = models.CharField(max_length=50, blank=True)
    image_url = models.CharField(max_length=200)
    active = models.BooleanField(
        default=False, help_text="Active means this image will display first in carousel")

    @property
    def object_id(self):
        value = self.title
        return '%s_%s' % (value.replace(" ", ""), self.id)

    # @classmethod
    def get_pages_by_id(cls, product_id):
        return cls.objects.filter(product=product_id)

    def __str__(self):
        return self.title


class Inquiry(models.Model):
    class ServiceChoices(models.TextChoices):
        PROGRAMMING = 'PR', _('Programming')
        DESIGNING = 'DE', _('Designing')
        FINANCIAL = 'FI', _('Financial')

    email = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=2, choices=ServiceChoices.choices)
    message = models.TextField(null=False)
    contact = models.CharField(max_length=50, blank=True, null=True)
    inquiry_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-inquiry_at"]
        verbose_name_plural = 'Inquiries'

    def __str__(self):
        return self.message[0:50]
