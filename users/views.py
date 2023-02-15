from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserRegisterForm, UserUpdateForm





def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

def user_login(request):   
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request=request, username=username, password=password)  # <User object> yoki None
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
     
    return render(request, "users/login.html")


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
#@csrf_exempt
def user_profile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            print('Form is valid!')
            form.save()    
        print('Form is invalid')
        return redirect('profile')    
    
    context = {
        'profile': user,
    }
    return render(request, 'users/profile.html', context)
