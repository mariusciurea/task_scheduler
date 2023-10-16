from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout, get_user


def user_login(request):

    user_login = True
    input_username = request.POST.get('username')
    input_password = request.POST.get('password')

    # print(input_username)
    # print(input_password)
    if request.method == 'POST':
        try:
            user = User.objects.get(username=input_username)
            user_auth = authenticate(request, username=input_username, password=input_password)
            if user_auth is not None:
                login(request, user_auth)
                return redirect('home')
            else:
                messages.error(request, 'Username or password does not exist!')
        except Exception:
            messages.error(request, "User does not exist!")

    context = {'user_login': user_login}
    return render(request, 'users/user_login.html', context)


def user_logout(request):
    current_user = request.user
    print(current_user)
    logout(request)
    messages.info(request, 'Successfully logged out!')
    return redirect('home')


def user_register(request):
    user_login = False

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

    context = {'user_login': user_login, 'form': form}

    return render(request, 'users/user_login.html', context)
