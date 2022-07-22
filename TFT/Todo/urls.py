# from django.contrib import admin
# from django.urls import path,include
from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="index"),
    path("remove/<id>",views.remove,name="remove"),
    path("complete/<id>",views.complete,name="complete"),
    path("not-complete/<id>",views.not_complete,name="not-complete"),
    path("sign_up",views.sign_up,name="sign_up"),
    path("sign_in",views.sign_in,name="sign_in"),

]
