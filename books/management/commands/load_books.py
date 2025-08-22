# your_app/management/commands/load_books.py
import json
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Load books from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        with open(json_file) as f:
            data = json.load(f)

        for item in data:
            Book.objects.create(
                title=item['title'],
                author=item['author'],
                description=item.get('description', ''),
                cover=item.get('image_url', '')
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded books data'))