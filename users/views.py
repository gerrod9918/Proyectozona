from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):

    if request.method == 'POST':
        print ('*' * 10)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('../lista/')
        else:
            return render(request,'users/login.html',{'error':'Usuario o contraseña invalidos'})


    return render(request,'users/login.html')

#@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
