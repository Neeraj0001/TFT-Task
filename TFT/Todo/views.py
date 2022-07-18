# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import todoForm
from .models import todoList
from django.http import HttpResponseRedirect
 
def index(request):
  print(request.method)
  if request.method=='POST':
    form=todoForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../Todo/")
    all_items=todoList.objects.all
    return render(request,'demo.html',{'lists':all_items})
  elif request.method=='GET':
    all_items=todoList.objects.all
    print(all_items)
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