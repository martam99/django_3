from django.core.management import BaseCommand

from Catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()

        new_categories = [
            {'category_name': 'Meat', 'category_description': 'Pork, Beef, Lamb, Chicken'},
            {'category_name': 'Dairy', 'category_description': 'Butter, Cheese, Ice Cream, Yogurt'}
            ]
        category_list = []
        for category in new_categories:
            category_list.append(Category(**category))

        Category.objects.bulk_create(category_list)
        print(category_list)
