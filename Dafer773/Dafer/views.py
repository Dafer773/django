from django.shortcuts import render

def helloworld(request):
    return render(request, 'helloworld.html')

def banana(request):
    return render(request, 'banana.html')

def abra(request):
    return render(request, 'abra.html')