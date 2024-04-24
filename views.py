from django.shortcuts import render

# Create your views here.

def bookapp(request):
    return render(request, 'url.html')