from django.shortcuts import render
from django.db.models import Sum

from adminapp.models import Product

# Create your views here.
def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество продуктов в базе данных',
        'total': total,
    }
    return render(request, 'installapp/total_count.html', context)


def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество продуктов в представлении',
        'total': total,
    }
    return render(request, 'installapp/total_count.html', context)


def total_in_template(request):
    context = {
        'title': 'Общее количество продуктов в шаблоне',
        'products': Product,
    }
    return render(request, 'installapp/total_count.html', context)
