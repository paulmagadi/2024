from django.shortcuts import render

# Create your views here.

def payment_sucess(request):
    return render(request, 'payment/payment_sucess.html')