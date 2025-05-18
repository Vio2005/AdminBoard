from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def sidebar(request):
    return render(request,'sidebar-style-2.html')

def icon(request):
    return render(request,'icon-menu.html')
