from django.shortcuts import render

from web.models import Product 

def index(request):

    products = Product.objects.all()

    context = {
        "products" : products,

    }
    return render(request, "index.html", context = context)  