from django.shortcuts import render, redirect
from store.models import Product
from .forms import ProductModelForm

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse



def admin_or_staff_required(view_func):
    """
    Decorator that checks if the user is an admin or staff member.
    """
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not (request.user.is_staff or request.user.is_superuser):
            return HttpResponse(status=401)  # Or redirect to login page or show a 401 error page
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# Usage example:
@admin_or_staff_required
def admin_portal(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'admin_portal/admin_portal.html', context)

@admin_or_staff_required
# def add_product(request):
#     return render(request, 'admin_portal/add_product.html')


def add_product(request):
    products = Product.objects.all()
    new_products = Product.objects.filter(is_new=True)
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    else:
        form = ProductModelForm()
    context = {
        'new_products ': new_products,'form': form, 'products': products
    }
    return render(request, 'admin_portal/add_product.html', context)