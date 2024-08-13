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
    lt =list(range(0,100))
    context["list"] = lt
    
    return render(request, 'test.html',context)

def cardclrPage(request):
    context = {
        'color': 'all',
    }  
    
    if request.method == "GET":
        color = request.GET.get('color')
        context = {'color': color}

    return render(request, 'card_color.html', context)


