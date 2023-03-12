from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, UserLoginForm
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'nonp/post_list.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('post_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'nonp/registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list')
            else:
                form.add_error(None, 'Invalid login credentials')
    else:
        form = UserLoginForm()
    return render(request, 'nonp/registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('post_list')

def stjude(request):
    return render(request, 'nonp/descriptions/stjude.html')

def afa(request):
    return render(request, 'nonp/descriptions/afa.html')

def woundedwarrior(request):
    return render(request, 'nonp/descriptions/woundedwarrior.html')

def riley(request):
    return render(request, 'nonp/descriptions/riley.html')

def t2t(request):
    return render(request, 'nonp/descriptions/t2t.html')

def redcross(request):
    return render(request, 'nonp/descriptions/redcross.html')

def wwf(request):
    return render(request, 'nonp/descriptions/wwf.html')

def feedingamerica(request):
    return render(request, 'nonp/descriptions/feedingamerica.html')

def ymca(request):
    return render(request, 'nonp/descriptions/ymca.html')

def donate(request):
    return render(request, 'nonp/post_list.html')
