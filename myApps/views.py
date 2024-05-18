from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import random
from django.core.mail import send_mail
from .models import PasswordManager,FormTest
from .forms import BlogForm

# Create your views here.
@login_required
def home(request):
    myinfo = PasswordManager.objects.filter(user=request.user)
    print(myinfo)
    # print(name)
    data = {'info':myinfo}
    return render(request,'home.html',data)

def loginUser(request): 
    if request.method=="POST":
        if "logsub" in request.POST:
            name = request.POST.get('name')
            passw= request.POST.get('pass')
            print(name,passw)
            myuser = authenticate(request,username=name,password=passw)
            print(myuser)
            if myuser is not None:
                login(request,myuser)
                return redirect('home')
        #         global code
        #         code = str(random.randint(11111,99999))
        #         send_mail('Confirm your Email ',f"Dear {name}, your Password Manager Login activation code is {code}",'pratham016914934@gmail.com',[myuser.email],fail_silently=False)
        #         return render(request,'active.html',{'code':code,'user':name})
        # elif "code_sub" in request.POST:
        #     mycode = request.POST.get('code')
        #     myname = request.POST.get('name')
        #     if mycode==code:
        #         login(request,User.objects.get(username=myname))
        #         return redirect(f'/home?name={myname}')
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        passw= request.POST.get('pass')
        conpass = request.POST.get('conpass')
        # print(name,email,passw,conpass)
        if len(passw)<=4:
            msg = "Password is too short"
            data = {'plmsg':msg}
            return render(request,'signup.html',data)
        elif passw!=conpass:
            msg = "password didn't matched"
            data = {'pmsg':msg}
            return render(request,"signup.html",data)
        elif User.objects.filter(username=name).exists():
            msg = "Username already exists"
            data = {'umsg':msg}
            return render(request,'signup.html',data)
        elif User.objects.filter(email=email).exists():
            msg = "Email already exists"
            data = {'emsg':msg}
            return render(request,'signup.html',data)
        else:
            myuser = User.objects.create_user(name,email,passw)
            myuser.save()
            return redirect('login')
    return render(request,'signup.html')

def loguser(request):
    logout(request)
    return redirect('login')

def mylist(request):
    name = request.GET.get('name')
    print(name)
    if request.method == "POST":
        aname = request.POST.get('aname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        passw = request.POST.get('password')
        pmanager = PasswordManager.objects.create(user=request.user,appname=aname,applink=lname,email=email,password=passw)
        pmanager.save()
        return redirect('home')
    return render(request,'mylist.html')

@login_required
def prac(request):
    data = {}
    mypost = FormTest.objects.all().order_by('-date')
    data['mypost']=mypost
    form = BlogForm()
    data['form']=form
    if request.method=='POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author=request.user
            newpost.save()
            return render(request,'practice.html',data)
    return render(request,'practice.html',data)