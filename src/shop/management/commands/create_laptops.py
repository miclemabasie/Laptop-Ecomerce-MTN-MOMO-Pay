import random
from django.core.management.base import BaseCommand
from shop.models import Laptop


class Command(BaseCommand):
    help = "creates some sample laptops"

    def handle(self, *args, **options):
        laptops = [
            {
                "brand": "Dell",
                "model_name": "Dell XPS",
                "description": "Powerful laptop with great battery life",
                "price": 1500,
            },
            {
                "brand": "Apple",
                "model_name": "MacBook Pro",
                "description": "Apple's flagship laptop for professionals",
                "price": 2000,
            },
            {
                "brand": "HP",
                "model_name": "HP Spectre",
                "description": "Sleek and stylish laptop with long battery life",
                "price": 1200,
            },
        ]

        for laptop_data in laptops:
            Laptop.objects.create(**laptop_data)
