from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
# from .forms import CreateUserForm
from django.contrib import messages


def register_user(request):
    return render(request, 'core/register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.sucess(request, ('Login sucess!'))
            return redirect('home')
        else:
            messages.success(request, ('Error Logging in. Try again!!!'))
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