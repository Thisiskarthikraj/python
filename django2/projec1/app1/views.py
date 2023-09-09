from django.shortcuts import render
from django.http import HttpResponse
from app1.models  import user
from app1.form import userform

def home(request):
    return render(request,"home.html")

def udetails(request):
    k=user.objects.all()
    return render(request,"form.html",{"s":k})

def frm(request):
    form=userform()
    if(request.method== "POST"):
        form=userform(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'upload.html',{"form":form})

# Create your views here.
