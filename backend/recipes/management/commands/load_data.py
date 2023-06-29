import csv
import os

from django.core.management import BaseCommand

from foodgram.settings import BASE_DIR
from recipes.models import Ingredient

MODELS_FILES = {
    Ingredient: 'ingredients.csv',
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = os.path.join(BASE_DIR, 'data/ingredients.csv')

        with open(file_path, encoding='utf-8') as table:
            reader = csv.reader(table)
            for row in reader:
                try:
                    Ingredient(name=row[0], measurement_unit=row[1]).save()
                except Exception as exc:
                    self.stdout.write(self.style.ERROR(
                        f'Ошибка при загрузке данных: {exc}')
                    )
        self.stdout.write(self.style.SUCCESS(
            'Ингредиенты успешно загружены')
        )
