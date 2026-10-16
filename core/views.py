from django.shortcuts import render
from .models import Product, Vendor, Client

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def all_products(request):
    products = Product.objects.all()
    ctx = {
        "products": products
    }
    return render(request, 'products.html', ctx)

def vendors(request):
    vendors = Vendor.objects.all()
    ctx = {
        "vendors": vendors
    }
    return render(request, 'vendors.html', ctx)

def clients(request):
    clients = Client.objects.all()
    ctx = {
        "clients": clients
    }
    return render(request, 'clients.html', ctx)
