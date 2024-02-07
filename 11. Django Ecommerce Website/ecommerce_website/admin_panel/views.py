from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

#register
def admin_signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    context = {'form': form}
    return render(request, 'signup.html', context)
    
    
    

# User Login    
def admin_signin(request):
    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None: 
                login(request, user)
                messages.success(request, ('Login sucess!'))
                return redirect('dashboard')
            else:
                messages.success(request, ('Error Logging in. Try again!!!'))
                return redirect('signin')
    else:
        return render(request, 'signin.html')
    
# User Logout  
def admin_signout(request):
    logout(request)
    messages.success(request, ('You have been logged out!!!'))
    return redirect('signin')

