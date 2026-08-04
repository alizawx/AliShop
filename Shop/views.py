from django. shortcuts import render, get_object_or_404
from . models import Category,Products

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category. objects.all()
    products = Products.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request,'shop/list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Products, slug=slug, id=id)
    return render(request,'shop/detail.html', {'product':product})