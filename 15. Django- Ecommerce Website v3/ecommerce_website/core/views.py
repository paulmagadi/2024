from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, UpdateUserForm
from django.contrib.auth.models import User


def update_user(request):
    if request.User.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.Post or None, instance=current_user) 
        
        if user_form.is_valid():
            user_form.save()
            
            login(request, current_user)
            messages.success(request, ("User Details updated"))
            return redirect('home')
        return render(request, 'core/update_user.html', {'user_form': user_form})
    else:
        messages.error(request, ("You must be logged in to update your details"))
    return render(request, 'core/update_user.html')

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
            messages.success(request, ('Registration sucessful. Login to continue'))
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Login successful!'))
            return redirect('home')  # Redirect to home if cart is empty or doesn't exist
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