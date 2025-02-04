from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Добавление продуктов а базу данных"

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(
            name="Ягоды", description="Описания ягод"
        )

        products = [
            {"name": "Голубика", "category": category, "price": 40},
            {"name": "Малина", "category": category, "price": 10},
        ]

        for products_data in products:
            product, created = Product.objects.get_or_create(**products_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Добавление продуктов произошло успешно {product.name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Продукты уже существуют {product.name}")
                )
