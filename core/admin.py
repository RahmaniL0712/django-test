from django.contrib import admin
from .models import Product, Vendor, Client, FormSubmissions

admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(Client)
admin.site.register(FormSubmissions)