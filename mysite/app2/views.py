from django.shortcuts import render

def index(request):
    return render(request, 'app2/index.html')

def services(request):
    return render(request, 'app2/services.html')