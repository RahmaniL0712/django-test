from django.shortcuts import render
from .forms import ContactForm
from .models import Product, Vendor, Client, FormSubmissions
from django.core.mail import send_mail

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm(request.POST or None)
    submitted = False
    if request.method == 'POST':
        if form.is_valid():
            print("Contact form submission:", form.cleaned_data)
            submitted = True
            created_form = {
                "name": form.cleaned_data.get("name"),
                "email": form.cleaned_data.get("email"),
                "message": form.cleaned_data.get("message"),
                "ip_address": request.META.get("REMOTE_ADDR")
            }
            FormSubmissions.objects.create(**created_form)
            send_mail(
                "Faleminderit per regjistrimin",
                f"Pershendetje {created_form.get("name")}! Te dhenat tuaja jane ruajtur me sukses.",
                "yourname@gmail.com",
                [
                    created_form.get("email")
                ],
                False
            )

    return render(request, 'contact.html', {
        "form": form,
        "submitted": submitted,
    })

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
