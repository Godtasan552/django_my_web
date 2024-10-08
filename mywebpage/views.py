from django.shortcuts import render, HttpResponse

# Create your views here.


def indexPage(request):
    return render(request, 'index.html')


def aboutPage(request):
    return render(request, 'about.html')


def contactPage(request):
    return render(request, 'contact.html')


def testPage(request):
    context = {}
    lt = list(range(0, 100))
    context["list"] = lt

    return render(request, 'test.html', context)


def cardclrPage(request):
    context = {
        'color': 'all',
    }

    if request.method == "GET" and request.GET.get('color') != None:
        color = request.GET.get('color')
        context = {'color': color}

    return render(request, 'card_color.html', context)


def testloopPage(request):
    context = {}
    lt = list(range(0, 100))
    context["list"] = lt

    return render(request, 'testloop.html', context)

def from_testPage(request):
    
    context ={
    "email":"",
    "password":""
    }
    
    if request.method == "GET":
        email = request.GET.get('email')
        password = request.GET.get('my_password')
        context = {
            "email":email,
            "password":password
        }
    return render(request, 'from.html',context)
