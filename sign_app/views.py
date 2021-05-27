from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm, SignInForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail

def home(request):
    if 'user' in request.session:
        return render(request, 'home.html')
    return redirect('sign_app:signin')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        # create sesstion variable
        request.session['user'] = username
        request.session['passwrod'] = password
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sign_app:home')
    form = SignInForm()
    return render(request, 'signin.html', {'form':form})

def signup(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            # create sesstion variable
            request.session['user'] = username
            request.session['passwrod'] = password
            user = authenticate(username=username, password=password)
            login(request, user)
            # redirect to home page
            return redirect('sign_app:home')

        # else
    form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

def log_out(request):
    if request.method == 'POST':
        request.session.flush()
    return redirect('sign_app:signin')

def error_404(request, exception):
    return render(request, '404.html')
