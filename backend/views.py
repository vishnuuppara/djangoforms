import imp
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import *

# Create your views here.

def home(request):
    return HttpResponse('hello world')
def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    return HttpResponse("my name {} and my age{}".format(name,age))

def firstpage(request):
    return render(request,'index.html')

def secondpage(request):
    return render(request,'secondpage.html')

def thirdpage(request):
    var='hello world'
    greting='how are you?'
    fruits=['banana','mango','graps']
    num1,num2=3,6
    mydic={'var':var,
    'msg':greting,'myfruits':fruits,'num1':num1,'num2':num2
    }
    return render(request,'thirdpage.html',mydic)

def firstimg(request,img):
    myfristimg=str(img)
    Myfristimg=myfristimg.lower()
    if Myfristimg == 'django':
       var=True
    else:
         Myfristimg == 'python'
         var =False
    my_dic={'var':var}
    return render (request,'firstimg.html',my_dic)

def secondimg(request):
    return render(request,'secondimg.html')
def form2(request):
    print("1")
    if request.method == "POST":
        print(".....")
        form =Feedback(request.POST)
        if form.is_valid():
            mydic={'form':Feedback()}
            tittle=request.POST['Tittle']
            subject=request.POST['subject']
            email=request.POST['email']
            
            print(tittle,subject)
            # var=str("form submittes"+ str(request.post))
            errorflag=False
            errors=[]
            if tittle!=tittle.upper():
                errorflag=True
                errormsg="tittle is in lowercase"
                errors.append(errormsg)
            import re
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not (re.search(regex, email)):
                errorflag=True
                errormsg="email is not vaild"
                errors.append(errormsg)
            if errorflag !=True:
                mydic['sucess']=True
                mydic['sucessmsg']='form submitted'
                return render(request,'form2.html',mydic)
            mydic['error']=errorflag
            mydic['errors']=errors
            return render(request,'form2.html',mydic )
        else:
            print("y")
            
        
            return render(request,'form2.html',{'form':form})
        
    else:
        print("3")
        form =Feedback()
        return render(request,'form2.html',{'form':form})
        


