from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Place
from .models import Team
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})


# def about(request):
#     return  render(request,'about.html')
# def contact(request):
#     return  HttpResponse('hewwwwww')
