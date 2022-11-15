from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    a = 5 + 6
    return render(request, 'about.html', {'gretting': a})


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['username']
    reverse = user_text[::-1]
    return render(request, 'reverse.html', {'word':reverse})
