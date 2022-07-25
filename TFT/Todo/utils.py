from django.core.mail import send_mail
from TFT import settings
import random

def send_mail_otp(mail_id,message,subject):
    send_mail(
        subject=subject,message=message,from_email=settings.EMAIL_HOST_USER, recipient_list=[mail_id,],fail_silently=False
    )
    return True
# def code_gen():
#     number_list=[x for x in range(10)]
#     code_items=[]
#     for i in range(5):
#         num=random.choice(number_list)
#         code_items.append(num)
#     code_string="".join(str(items) for items in code_items)
#     return code_string
