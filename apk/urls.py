from .views import *
from django.urls import path,include

urlpatterns = [

    path('',home,name='pro'),
    path('catagory/<str:ok>',pro,name='catag'),
]
