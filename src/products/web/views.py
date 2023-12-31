from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from .models import Product
from .forms import ProductForm


def index(request):
    products = Product.objects.all()
    context = {"products" : products}
    return render(request, "index.html", context = context)  


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("web:index")
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,  request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('web:index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})


def product_delete(request, pk):
    user = get_object_or_404(User)
    if request.user.is_authenticated and user.is_staff:
        product = get_object_or_404(Product, pk=pk)
        product.delete()
    return redirect('web:index')