from celery import shared_task
from django.shortcuts import render, redirect
from .models import todoList
from django.http import HttpResponseRedirect
from PIL import Image



@shared_task(bind=True)
def check_task_image(self,task_id):
    task=todoList.objects.get(pk=task_id)
    img=Image.open(task.picture)
    temp=img.format
    l=['jpg','jpeg','png','gif','JPG','JPEG','PNG','GIF']
    if temp in l:
        task.description="Valid Image file"
        task.save()
    else:
        task.description="Not a Valid Image file, Please Delete this field !!!!!1"
        task.save()
    return redirect("index")
    # form=todoForm(task,picture)
    # # print(form.cleaned_data.get('picture'))
    # if form.is_valid():
    #     temp=form.save(commit=False)
    #     temp.user=user
    #     temp.save()
    #     return HttpResponseRedirect("../Todo/")
    # all_items=todoList.objects.filter(user=user)
    # print(all_items)
