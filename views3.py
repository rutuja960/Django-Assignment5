from django.shortcuts import render
from . import forms
from . import models
def loginpage(request):
    f1=forms.MyForm()
    return render(request,"login.html",{'form':f1})
def getdata(request):
    if request.method=='POST':
        un=request.POST['fname']
        p=request.POST['lname'] 
        s1=models.Student(fname=un,lname=p)
        s1.save()
        form=MyForm(request.POST)
        if form.is_valid():
            messages.success(request,'The form is valid.')
        else:
            messages.error(request,'The form is invalid.')
        return render(request,"login.html",{"fname":un,"lname":p})   