from books.models import Book
import json
import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import books from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('data_file', type=str, help='Path to the JSON file')
        
    def handle(self, *args, **options):
        data_file = options['data_file']
        ext = os.path.splitext(data_file)[1].lower()

        if ext != '.json':
            self.stdout.write(self.style.ERROR('Only JSON files are supported.'))
            return

        with open(data_file, 'r', encoding='utf-8') as file:
            books = json.load(file)
            for entry in books:
                title = entry.get('title')
                author = entry.get('author')
                cover = entry.get('image_url')

                if title and author:
                    Book.objects.get_or_create(
                        title=title,
                        author=author,
                        cover=cover
                    )
                    self.stdout.write(self.style.SUCCESS(f'Imported book: {title}'))