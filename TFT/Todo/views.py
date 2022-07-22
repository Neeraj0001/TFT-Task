# from django.http import HttpResponse
from email import message
import imp
from django.shortcuts import render, redirect
from .forms import todoForm
from django.contrib import messages
from .models import todoList
from django.http import HttpResponseRedirect
from Accounts.models import Users
from django.contrib.auth import authenticate,login,logout

def index(request):
  if request.method=='POST':
    form=todoForm(request.POST)
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
        message.info(request,"Invalid Credential !!!")
        return redirect('sign_in')
    return render(request,'sign_in.html')


def sign_out(request):
  logout(request)
  return redirect('sign_in')