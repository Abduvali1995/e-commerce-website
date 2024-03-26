from django.shortcuts import render,redirect
from .forms import RegistartionForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistartionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=RegistartionForm
    return render(request, 'register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return  redirect('/')