from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'StoreApp/index.html', {'products': products})

def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'StoreApp/show.html', {'product': product})
