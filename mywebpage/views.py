from django.shortcuts import render, HttpResponse

# Create your views here.


def indexPage(request):
    return HttpResponse("Hello, This is my web")


def aboutPage(request):
    return HttpResponse("เกี่ยวกับฉัน")


def contactPage(request):
    return HttpResponse("ติดต่อฉัน")
