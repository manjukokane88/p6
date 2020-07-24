from django.shortcuts import render
from django.http import HttpResponse
from math import factorial

# Create your views here.


def demo1(request):
    return render(request,'myapp/demo1.html')

def demo2(request):
    return render(request,'myapp/demo2.html',{'name':'manju'})

def fact(request,n):
    n=int(n)
    return HttpResponse("<h2>factorial is {}</h2>".format(factorial(n)))       


