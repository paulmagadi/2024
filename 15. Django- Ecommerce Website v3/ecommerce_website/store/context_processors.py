from .models import Product, Category

def categories(request):
    # categories = Category.objects.values_list('name', flat=True).distinct()
    categories = Category.objects.all()
    return {'categories': categories}


