from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, UpdateUserForm, UpdateUserPassword, UpdateInfoForm, ShippingAddressForm
from django.contrib.auth.models import User
from store.models import Profile, ShippingAddress
import json
from cart.cart import Cart


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
            
            user = authenticate(username=email, password=password)
            login(request, user)
            messages.success(request, ('User created. Please fill in your Shipping info'))
            return redirect('update_info')
            # messages.success(request, ('Registration sucessful. Login to continue'))
            # return redirect('login')
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
            
            #Shopping cart
            current_user = Profile.objects.get(user__id=request.user.id)
            # Get saved cart from the model
            saved_cart = current_user.old_cart
            if saved_cart:
                #Convert the string back  to dictionary using JSON
                converted_cart = json.loads(saved_cart)
                
                #Add to session
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

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

def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UpdateInfoForm(request.POST or None, instance=current_user)
        
        if form.is_valid():
            form.save()
            messages.success(request, ("Your info has been updated"))
            return redirect('home')
        return render(request, 'core/update_info.html', {'form': form})
    else:
        messages.error(request, ("You must be logged in to update your info"))
    return render(request, 'core/update_info.html')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = UpdateUserPassword(current_user ,request.POST) 
            
            if form.is_valid():
                form.save()
                messages.success(request, ("Your password has been updated. Login with your new password"))
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
                     
        else:
            form = UpdateUserPassword(current_user)
            return render(request, 'core/update_password.html', {'form': form})
    else:
        messages.error(request, ("You must be logged in to update your password"))
        return redirect('home')

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user) 
        
        if user_form.is_valid():
            user_form.save()
            
            login(request, current_user)
            messages.success(request, ("User Details updated"))
            return redirect('home')
        return render(request, 'core/update_user.html', {'user_form': user_form})
    else:
        messages.error(request, ("You must be logged in to update your details"))
        return redirect('home')


    return redirect('home')


def user_profile(request):
    return render(request, 'core/user_profile.html')

def shipping_info(request):
    if request.user.is_authenticated:
        current_user = ShippingAddress.objects.get(user__id=request.user.id)
        form = ShippingAddressForm(request.POST or None, instance=current_user)
        
        if form.is_valid():
            form.save()
            messages.success(request, ("Your info has been updated"))
            return redirect('home')
        return render(request, 'core/shipping_information.html', {'form': form})
    else:
        messages.error(request, ("You must be logged in to update your info"))
    return render(request, 'core/shipping_information.html')