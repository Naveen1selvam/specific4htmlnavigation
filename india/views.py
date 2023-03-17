from django.shortcuts import render

# Create your views here.
def bcci(request):
    return render(request,'bcci.html')
def ipl(request):
    return render(request,'ipl.html')
