from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def index(request):
    return render (request,'index.html')
def page1(request):
    return render (request,'Bootstrapvideos.html')
def page2(request):
    return render (request,'contactt.html')
def page3(request):
    return render (request,'CSSvideos.html')
def page4(request):
    return render (request,'Database.html')
def page5(request):
    return render (request,'Dsuvideos.html')
def page6(request):
    return render (request,'Gitvideos.html')
def page7(request):
    return render (request,'Htmlvideos.html')
def page8(request):
    return render (request,'Linuxvideos.html')
def page9(request):
    return render (request,'Python.html')
def page10(request):
    return render (request,'Photoshop.html')
def page11(request):
    return render (request,'Reactjs.html')
def contact(request):
    return render (request,'contactt.html')



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')