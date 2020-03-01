from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('/',home,name="cat-home"),
    path('/',create,name="cat-create"),
    path('/',edit,name="cat-edit")

]