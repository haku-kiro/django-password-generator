from django.shortcuts import render
from django.http import HttpResponse
import random
import string


# Create your views here.
def home(request):
    # Looks for our templates directory
    return render(request, 'generator/home.html')


def password(request):

    # This is how you access request arguments
    length = int(request.GET.get('length'), 12)
    chars = string.ascii_lowercase

    if request.GET.get('uppercase'):
        chars = string.ascii_letters
    if request.GET.get('special'):
        # Just taking out backslashes
        chars += string.punctuation.replace('\\', '')
    if request.GET.get('numbers'):
        chars += string.digits

    pwd = "".join([random.choice(chars) for x in range(length)])

    return render(request, 'generator/password.html', {"password": pwd})


def about(request):
    return render(request, 'generator/about.html')


def example(request):
    # return render(request, 'generator/home.html', {"password": "something"})
    return HttpResponse("Hello there!")
