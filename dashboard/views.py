from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from home.models import Inquiry


def home(request):
    context = {}
    return render(request, "base/dashboard.html", context)


@login_required(login_url='login')
def inquiry(request):

    inquiries = Inquiry.objects.all()

    context = {"inquiries": inquiries}
    return render(request, "base/inquiry.html", context)
