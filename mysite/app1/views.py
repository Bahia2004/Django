from django.shortcuts import render

def index(request):
    return render(request, 'app1/index.html')

def about(request):
    return render(request, 'app1/about.html')

def contact(request):
    return render(request, 'app1/contact.html')
def home(request):
    return render(request, 'app1/home.html')