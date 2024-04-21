from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/show.html', {'product': product})
