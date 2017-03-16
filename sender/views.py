
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import SendForm
from .models import Message


@login_required()
def index(request):
    u"""
    Main send form page,
    """
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            msg = Message()
            result = msg.send(form.cleaned_data['text'], form.cleaned_data['email'])
            form.clean()
        else:
            result = form.errors
        return render(request, 'index.html', {'form': form, 'msg': result})
    else:
            form = SendForm(initial={'email': request.user.email})
            return render(request, 'index.html', {'form': form})


def login_page(request):
    u"""
    Login form render, recieving POST requests for user validate
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user.is_active:
                login(request, user)
            data = {'is_ok': True}
        else:
            data = {'is_ok': False, 'msg': form.errors}
        return JsonResponse(data)
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def register_page(request):
    u"""
    Register form render, recieving POST requests for user check
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            data = {'is_ok': True}
        else:
            data = {'is_ok': False, 'msg': form.errors}
        return JsonResponse(data)
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
