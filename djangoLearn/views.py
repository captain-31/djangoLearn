from django.http import HttpResponse
from django.shortcuts import render
from .models import Work


def home(request):
    # Old code
    # return HttpResponse("Hello World")
    return render(request, "home.html", {"name": "Captain"})


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2

    return render(request, "result.html", {"result": res})
    # return HttpResponse(res)


def index(request):

    wrks = Work.objects.all()

    return render(request, "index.html", {'wrks': wrks})


def material(request):
    return render(request, "material.html")
