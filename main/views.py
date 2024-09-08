from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306123456',
        'name': 'Pak Bepe',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

def categories(request):
    return render(request, 'categories.html')

def products(request):
    return render(request, 'products.html')

def cart(request):
    return render(request, 'cart.html')
