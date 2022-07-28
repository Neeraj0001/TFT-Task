from celery import shared_task
from django.shortcuts import render, redirect
from .models import todoList
from django.http import HttpResponseRedirect
from PIL import Image
import easyocr
import pytesseract

@shared_task(bind=True)
def check_task_image(self,task_id):
    print(self,task_id)
    task=todoList.objects.get(pk=task_id)
    img=Image.open(task.picture)
    pytesseract.pytesseract.tesseract_cmd = r'''C:\Program Files\Tesseract-OCR\tesseract.exe'''
    custom_config = r'-l eng --oem 3 --psm 6' 
    text = pytesseract.image_to_string(img,config=custom_config)
    print(len(text))
    if len(text)!=0:
       task.description=text
    else:
        task.description="No Text in the image"
    task.save()  



@shared_task(bind=True)
def check_image_format(self,task_id):
    task=todoList.objects.get(pk=task_id)
    img=Image.open(task.picture)
    temp=img.format
    print(temp)
    path="media/"+str(task.picture)
    l=['jpg','jpeg','png','gif','JPG','JPEG','PNG','GIF']
    if temp in l:
        task.img_format_valid=True
    else:
        task.img_format_valid=False
    task.save()

    # temp=img.format
    # path="media/"+str(task.picture)
    # l=['jpg','jpeg','png','gif','JPG','JPEG','PNG','GIF']
    # if temp in l:
    #     reader = easyocr.Reader(['en'])
    #     result = reader.readtext(path)
    #     st=""
    #     for detection in result: 
    #         text = detection[1]
    #         st+=text+","
    #     print(st)
    #     if len(st)!=0:
    #         task.description=st
    #     else:
    #         task.description="No Text in the image"
    #     task.save()
    # else:
    #     task.description="Not a Valid Image file, Please Delete this field !!!!!1"
    #     task.save()


