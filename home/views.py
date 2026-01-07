from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

# Create your views here.
def home(request):
    home=Category.objects.filter()
    return render(request,'index.html',{"home":home})
def category(request):
    category=Category.objects.filter()
    return render(request,"categories.html",{"category":category})
def about(request):
    return render(request,'about Us.html')
def contact(request):
    return render(request,'contact.html')
def views(request):
    return render(request,'views.html')
def sweet_details(request, cname, pname):

    if not Category.objects.filter(name=cname).exists():
        messages.error(request, "No Such Category Found")
        return redirect("category")

    if not Sweet.objects.filter(name=pname).exists():
        messages.error(request, "No Such Product Found")
        return redirect("category")

   

