from django.shortcuts import render
from . import forms
from . import models

# Create your views here.
def registrationpage(request):
    return render(request,"register.html")

def getdata(request):
   
    if request.method=='GET':
        un=request.GET['fname']
        p=request.GET['lname'] 
        e=request.GET['email']
        n=request.GET['phone']    
        return render(request,"register.html",{"fname":un,"lname":p,"email":e,"phone":n})   

    if request.method=='POST':
        un=request.POST['fname']
        p=request.POST['lname']
        e=request.POST['email']
        n=request.POST['phone'] 
        s1=models.Student(fname=un,lname=p,email=e,phone=n)
        s1.save()
        return render(request,"register.html",{"fname":un,"lname":p,"email":e,"phone":n})   
