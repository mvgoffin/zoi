from django.shortcuts import render

# Create your views here.
def home(request):
    context = locals()
    template = 'home.html'
    return render(request,template,context)

def about(request):
    context = locals()
    template = 'about.html'
    return render(request,template,context)

def success(request):
    context = locals()
    template = 'success.html'
    return render(request,template,context)

def access_code_granted(request):
    context = locals()
    template = 'access_code_granted.html'
    return render(request,template,context)

