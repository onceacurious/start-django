from itertools import product
from django.shortcuts import render, redirect
from django.db.models import Q

from home.forms import InquiryRoom

from .models import ProductCard, ProductPage


def home(request):
    cards = ProductCard.objects.all()
    pages = ProductPage.objects.all()
    form = InquiryRoom()

    if request.method == "POST":
        form = InquiryRoom(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"cards": cards, "pages": pages, "form": form}
    return render(request, "base/home.html", context)
