from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import resolve

from home.models import Inquiry


def home(request):
    current_url = resolve(request.path_info).url_name
    print(current_url)
    context = {"url_logger": url_logger(current_url)}
    return render(request, "base/dashboard.html", context)


@login_required(login_url='login')
def inquiry(request):

    inquiries = Inquiry.objects.all()
    current_url = resolve(request.path_info).url_name

    context = {"inquiries": inquiries, "url_logger": url_logger(current_url)}
    return render(request, "base/inquiry.html", context)


def url_logger(name: str):
    '''
        Getting url path to display something or hide something
    '''
    url_list = ['dashboard', 'inquiry']
    if url_list.index(name.strip()) >= 0:
        return True
    else:
        return False
