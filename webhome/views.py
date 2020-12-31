from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request, 'webhome/content.html')

def nav(request):
    return render(request,"webhome/nav.html")
def css(request):
    return render(request,"webhome/css.html")
def footer(request):
    return render(request,"webhome/footer.html")
def javascript(request):
    return render(request,"webhome/javascript.html")
def popup(request):
    return render(request,"webhome/popup.html")
def base(request):
    return render(request,"webhome/base.html")