from django.contrib import admin

from .models import Inquiry, ProductCard, ProductPage


admin.site.register(ProductCard)
admin.site.register(ProductPage)
admin.site.register(Inquiry)
