from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import *
# Create your views here.
def error_404_view(request,exception):
    return render(request,'404.html')
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

def myimgpage2(request,imgname):
    myimage = imgname
    myimage = imgname.lower()

    if myimage == "asx":
        var = True
    elif myimage == "dog":
        var = False
    mydict = {
        "var" : var
    }

    return render(request, 'imagepage2.html',mydict)

def myform(request):
    return render(request, 'myform.html')

def submitmyform(request):
    mydict = {
        "var1": request.POST['mytext'],
        "var2": request.POST['mytextarena'],
        "method": request.method
    }

    return JsonResponse(mydict)

def myform2(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            # var = str("Form Submitted" + str(request.method))
            # return HttpResponse(var)
            mydict = {
                "form": FeedbackForm()
            }
            errorflag = False
            Error = []
            if title != title.upper():
                errorflag = True
                errormsg = "Title should be Capital"
                Error.append(errormsg)
            import re
            regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.search(regex,email):
                errorflag = True
                errormsg = "Not a valid email address"
                Error.append(errormsg)
            if errorflag != True:         
                mydict['success'] = True
                mydict['successmsg'] = "Form Submitted"
            
            mydict['error'] = errorflag
            mydict['errors'] = Error 
            return render(request, 'myform2.html', mydict)
        # else:
        #     mydict = {
        #         "form":form
        #     }
        #     return render(request,'myform2.html',mydict)
    elif request.method == "GET":
        form = FeedbackForm()
        mydict = {
            "form":form
        }
        return render(request, 'myform2.html', mydict)