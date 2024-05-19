from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')  # Redirect to a success page or homepage
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'register.html', {'form': form})
