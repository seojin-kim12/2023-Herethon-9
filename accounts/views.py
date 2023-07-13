from django.shortcuts import render, redirect
from .models import CustomUser, CustomUserManager
from django.contrib import auth
from django.contrib.auth import login, authenticate

#회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            user = CustomUser.objects.create_user(
                custom_id=request.POST['custom_id'],
                password=request.POST['password'],
                username=request.POST['username'],
            )
            auth.login(request, user)
            return redirect('login')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

#로그인
def login(request):
    if request.method == 'POST':
        custom_id = request.POST['custom_id']
        password = request.POST['password']
        user = auth.authenticate(request, custom_id=custom_id, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home.html')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

#로그아웃
def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')
