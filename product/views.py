from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Count, Q
from .models import (
    Product, ProductImages, Category
)


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    products = Product.objects.all()
    category_list = Category.objects.annotate(total_product=Count('product'))

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)

    search_query = request.GET.get('q')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(condition__icontains=search_query) |
            Q(brand__brand_name__icontains=search_query) |
            Q(category__category_name__icontains=search_query) 
        )

    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        "products": products,
        "category_list": category_list,
        "category": category,

    }

    return render(request, 'product/product_list.html', context=context)


def product_details(request, product_slug):
    products = Product.objects.get(slug=product_slug)
    productImages = ProductImages.objects.filter(product=products)
    context = {
        "products_dtls": products,
        "productImages": productImages,
    }

    return render(request, 'product/product_details.html', context=context)
