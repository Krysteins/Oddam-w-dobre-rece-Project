from django.shortcuts import render


def landing(request):
    return render(request, "index.html")


def donation(request):
    return render(request, "form.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")
