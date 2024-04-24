from django.http import HttpResponse
from django.shortcuts import render

from cricket.models import Contact


# Create your views here.

def index(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is home page")

def stats(request):
    return render(request,'stats.html')

def teams(request):
    return render(request,'teams.html')

def pointtable(request):
    return render(request,'pointtable.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact= Contact(name=name,email=email,message=message)
        contact.save()
        
    return render(request,'contact.html')

def csk(request):
    return render(request,'Teams/csk.html')

def dc(request):
    return render(request,'Teams/dc.html')

def gt(request):
    return render(request,'Teams/gt.html')

def kkr(request):
    return render(request,'Teams/kkr.html')

def lsg(request):
    return render(request,'Teams/lsg.html')

def mi(request):
    return render(request,'Teams/mi.html')

def punjab(request):
    return render(request,'Teams/punjab.html')

def rr(request):
    return render(request,'Teams/rr.html')

def rcb(request):
    return render(request,'Teams/rcb.html')

def srh(request):
    return render(request,'Teams/srh.html')
