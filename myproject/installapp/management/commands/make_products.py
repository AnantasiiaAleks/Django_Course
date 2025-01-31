from random import choice, randint, uniform

from django.core.management.base import BaseCommand
from adminapp.models import Category, Product


class Command(BaseCommand):
    help = "Generate fake products"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество продуктов для генерации')

    def handle(self, *args, **options):
        categories = Category.objects.all()
        products = []
        count = options.get('count')
        for i in range(1, count + 1):
            products.append(Product(
                name=f'Продукт номер {i}',
                category=choice(categories),
                description='Длинное описание продукта, которое все равно никто не читает',
                price=uniform(0.01, 999_999.99),
                quantity=randint(1, 10_000),
                rating=uniform(0.01, 9.99),
            ))
        Product.objects.bulk_create(products)