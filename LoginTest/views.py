from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def result(request):
    username=request.POST['username']
    return render(request,'result.html',{'username':username})