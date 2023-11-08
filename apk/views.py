from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def home(request):
    cata=Catagory.objects.all()
    brand=Brand.objects.all()
    al=Catagory.objects.filter(name__icontains='mobile')
    print(al)
    return render(request,'index.html',{'al':all,'cata':cata,'brand':brand})

def pro(request,ok):
    cat=Catagory.objects.filter(name__icontains=ok)
    band=Brand.objects.filter(name__icontains=ok)

    if band.exists:
        allpro=Product.objects.filter(brand__in=band)

    if cat.exists:
        allpro=Product.objects.filter(catagory__in=cat)

    return render(request,'pro.html',{'cat':allpro})