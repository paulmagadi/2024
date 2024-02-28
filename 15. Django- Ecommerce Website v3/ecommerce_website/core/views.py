from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.models import User


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]  # Assuming the email field is named "email" in your login form
        password = request.POST["password"]
        user = authenticate(username=email, password=password)  # Use email as the username
        if user is not None:
            login(request, user)
            messages.success(request, ('Login successful!'))
            return redirect('home')
        else:
            messages.error(request, ('Error logging in. Please try again.'))
            return redirect('login')
    else:
        return render(request, 'core/login.html')


# User Logout  
def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!!!'))
    return redirect('home')

# user Registration
# def register_user(request):
#     form = CreateUserForm()
#     if request.method == "POST":
#         form = CreateUserForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('home')
            
#     return render(request, 'store/register.html', {'form': form})