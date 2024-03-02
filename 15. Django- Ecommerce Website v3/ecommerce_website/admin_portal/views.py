from django.shortcuts import render

# Create your views here.

def admin_portal(request):
    return render(request, 'admin_portal/admin_portal.html')