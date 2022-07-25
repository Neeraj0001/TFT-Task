# from django.contrib import admin
# from django.urls import path,include
from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="index"),
    path("edit_details",views.edit_details,name="edit_details"),
    path("remove/<id>",views.remove,name="remove"),
    path("complete/<id>",views.complete,name="complete"),
    path("not-complete/<id>",views.not_complete,name="not-complete"),
    path("update/<id>",views.update,name="update"),
    path("sign_up",views.sign_up,name="sign_up"),
    path("sign_in",views.sign_in,name="sign_in"),
    path('logout', views.sign_out,name="sign_out"),
    path('send_otp',views.send_otp,name="send_otp"),
    path('verify_otp/<str:email>',views.verify_otp,name="verify_otp"),
    path('resend_otp/<str:email>',views.resend_otp,name="resend_otp"),
]
