from django.shortcuts import render
from .models import Product, Vendor

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    all_products = Product.objects.all()
    all_vendors = Vendor.objects.all()
    return render(request, 'products.html', {'products': all_products,
                                             'vendors': all_vendors})