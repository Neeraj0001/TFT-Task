# from django.http import HttpResponse
from email import message
import imp
import re
from django.shortcuts import render, redirect
from .forms import todoForm,customForm
from django.contrib import messages
from .models import todoList
from django.http import HttpResponseRedirect
from Accounts.models import Users,Code
from django.contrib.auth import authenticate,login,logout
from .utils import send_mail_otp
from django.contrib.auth.hashers import check_password

def index(request):
  if request.method=='POST':
    form=todoForm(request.POST,request.FILES)
    print(form.is_valid)
    if form.is_valid():
        temp=form.save(commit=False)
        temp.user=request.user
        temp.save()
        return HttpResponseRedirect("../Todo/")
    all_items=todoList.objects.filter(user=request.user)
    return render(request,'demo.html',{'lists':all_items})
  elif request.method=='GET':
    all_items=todoList.objects.filter(user=request.user)
    return render(request,'demo.html',{'lists':all_items})


def remove(request,id):
    item=todoList.objects.get(pk=id)
    item.delete()
    return redirect('index')


def complete(request,id):
    item=todoList.objects.get(pk=id)
    item.action=True
    item.save()
    return redirect('index')


def not_complete(request,id):
    item=todoList.objects.get(pk=id)
    item.action=False
    item.save()
    return redirect('index')

def update(request,id):
    item=todoList.objects.get(pk=id)
    item.action=False
    item.save()
    return redirect('index')

def sign_up(request):
  print(request.method)
  if request.method=='POST':
    full_name=request.POST['full_name'].split()
    first_name=full_name[0]
    last_name=full_name[1]
    email=request.POST['email']
    password1=request.POST['password1']
    password2=request.POST['password2']
    if password1==password2:
      if Users.objects.filter(email=email).exists():
        messages.info(request,'Email Address Already taken !!!')
        return redirect('sign_up')
      else:
        user=Users.objects.create_user(email=email,password=password1,first_name=first_name,last_name=last_name)
        user.save()
        Code.objects.create(user=user)
        messages.info(request,'User Created')
        return redirect('sign_in')
    else:
        messages.info(request,'Password not matched !!!')
        return redirect('sign_up')

  return render(request,'sign_up.html')


def sign_in(request):
    print(request.method)
    if request.method=='POST':
      email=request.POST['email']
      password=request.POST['password']
      user=authenticate(email=email,password=password)
      print(user)
      if user is not None:
        login(request,user)
        return redirect("index")
      else:
        messages.info(request,"Invalid Credential !!!")
        return redirect('sign_in')
    return render(request,'sign_in.html')


def sign_out(request):
  logout(request)
  return redirect('sign_in')


def send_otp(request):
  if request.method=="POST":
    email=request.POST['email']
    user=Users.objects.filter(email=email)
    val=user.exists()
    print(val)
    if val:
      user=Users.objects.get(email=email)
      Code.objects.get(user=user).save()
      code=Code.objects.get(user=user).otp
      msgs="Hii !!, Your One Time Password to login in TFT is "+str(code)
      sub="One Time Password"
      send_mail_otp(user.email,msgs,sub)
      return redirect('verify_otp',email=user.email)
      
    else:
      messages.info(request,"Invalid Email Id !!!")
      return redirect("send_otp")
      ###
  return render(request,"otp.html")

def verify_otp(request,email):
  print(request)
  if request.method=="POST":
    email=email
    print(email)
    user=Users.objects.get(email=email)
    otp=request.POST["otp"]
    password1=request.POST["password1"]
    password2=request.POST["password2"]
    
    code=Code.objects.get(user=user)
    if (str(code.otp)==otp):
      if (password1==password2):
        password=user.password
        print(check_password(password1,password))
        if not check_password(password,password1):
          user.set_password(password1)
          user.save()
          
          # messages.info("Pasword Updated !!!")
          return redirect('sign_in')
        else:
          messages.info("Same Password as previously used")
          return redirect('verify_otp',email=user.email)
      else:
        messages.info("Password didn't matched")
        return redirect('verify_otp',email=user.email)
    else:
      messages.info("OTP didn't matched")
      return redirect('verify_otp',email=user.email)
  else:
    return render(request,"password.html",{'email':email})


def resend_otp(request,email):
  user=Users.objects.get(email=email)
  Code.objects.get(user=user).save()
  code=Code.objects.get(user=user).otp
  msgs="Hii !!, Your One Time Password to login in TFT is "+str(code)
  sub="One Time Password"
  send_mail_otp(user.email,msgs,sub)
  return redirect('verify_otp',email=user.email) 
      
def edit_details(request):
  user=request.user
  form=customForm(instance=user)
  if request.method =="POST":
    form=customForm(request.POST,request.FILES,instance=user)
    if form.is_valid():
      form.save()
  context={'form':form}
  return render(request,'edit_detail.html',context)


    



