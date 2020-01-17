from django.shortcuts import render
from .forms import LoginForm, SignupForm, ResetPasswordForm, MyCustomLoginForm, MyCustomSignupForm, MyCustomSetPasswordForm

# Create your views here.
def home(request):
    return render(request, 'index.html')


def login(request):
    form = MyCustomLoginForm()
    return render(request, 'account/login.html', {'form':form})

def signup(request):
    form = MyCustomSignupForm()
    return render(request, 'account/signup.html', {'form':form})
