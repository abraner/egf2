from django.shortcuts import render
#from django.core.mail import send_mail


def index2(request):
    context = {}
    return render(request, 'egf/index2.html', context)

def home(request):
    return render(request, 'egf/home.html')


def index(request):
    return render(request, 'egf/index.html')


def base(request):
    return render(request, 'egf/base2.html')
