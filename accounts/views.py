from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists ❌")
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        return redirect('/')

    return render(request, 'signup.html')