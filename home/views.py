from itertools import product
from django.shortcuts import render
from django.db.models import Q

from .models import ProductCard, ProductPage


def home(request):
    cards = ProductCard.objects.all()
    context = {"cards": cards}
    return render(request, "base/home.html", context)


def pages(request, pk):
    card = ProductCard.objects.get(id=pk)
    # pages = (product=card.id)
    print(card)
    context = {"pages": pages}
    return render(request, "base/web_dev_carousel.html", context)
