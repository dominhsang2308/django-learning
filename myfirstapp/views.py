from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello Worlds")

def myfunctionabout(request):
    return HttpResponse('About')

def myfuncintro(request,name,age):
    mydict = {
        'name': name,
        'age' : age
    }
    return JsonResponse(mydict)

def myfirstpage(request):
    return render(request,'index.html')

def mysecondpage(request):
    return render(request, 'secondpage.html')

def mythirdpage(request):
    greeting = 'how are you'
    myfruits = ['banana','mango','berry']
    num1,num2 = 3,5
    ans = num1 < num2 #False
    mydict = {
        'greet' : greeting,
        'fruits': myfruits,
        'num1': num1,
        'num2':num2,
        'ans': ans
    }
    return render(request, 'third.html', context=mydict)

def myimgpage(request):
    return render(request, 'imagepage.html')