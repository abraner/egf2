from django.shortcuts import render
from django.core.mail import send_mail


def index2(request):
    context = {}
    return render(request, 'egf/index2.html', context)

def home(request):
    return render(request, 'egf/home.html')


def index(request):
    return render(request, 'egf/index.html')


def base(request):
    return render(request, 'egf/base2.html')


def about(request):
    return render(request, 'egf/about.html')


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['elitegunfitting@gmail.com'],  # To Email
            )

        return render(request, 'egf/contact.html', {'message_name': message_name})

    else:
        return render(request, 'egf/contact.html', {})


def services(request):
    return render(request, 'egf/services.html')


def evaluation(request):
    return render(request, 'egf/evaluation.html')
