from django.shortcuts import render
from .models import Product, Category 

def show_main(request):
    context = {
        'npm' : '2306123456',
        'name': 'Pak Bepe',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

def account_page(request):
    return render(request, 'account.html')

def products_page(request):
    return render(request, 'products.html')

def cart_page(request):
    return render(request, 'cart.html')

def product_list(request):
    selected_category = request.GET.get('category')
    categories = Category.objects.all()
    
    if selected_category:
        products = Product.objects.filter(category__name=selected_category)
    else:
        products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
        'selected_category': selected_category
    }
    return render(request, 'products.html', context)
