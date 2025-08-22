import json
import os
from django.core.management.base import BaseCommand
from books.models import Book # Replace 'your_app_name' and 'Book'

class Command(BaseCommand):
    help = 'Imports book data from a JSON file into the database.'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The path to the JSON file to import.')

    def handle(self, *args, **kwargs):
        json_file_path = kwargs['json_file']
        
        # Check if the file exists
        if not os.path.exists(json_file_path):
            self.stdout.write(self.style.ERROR(f'File not found: {json_file_path}'))
            return

        self.stdout.write(self.style.NOTICE(f'Starting import from {json_file_path}...'))

        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                books_data = json.load(f)

            books_created = 0
            for book_data in books_data:
                # Get the values from the JSON data.
                # Use .get() to avoid key errors if a field is missing.
                title = book_data.get('title')
                author = book_data.get('author')
                image_url = book_data.get('image_url')

                if not title:
                    self.stdout.write(self.style.WARNING(f"Skipping a book entry with a missing title: {book_data}"))
                    continue

                # Create a new Book instance in the database
                book, created = Book.objects.get_or_create(
                    title=title,
                    defaults={
                        'author': author,
                        'image_url': image_url,
                    }
                )

                if created:
                    books_created += 1
                    self.stdout.write(self.style.SUCCESS(f'Successfully created book: {title}'))
                else:
                    self.stdout.write(f'Book already exists, updating: {title}')
                    book.author = author
                    book.image_url = image_url
                    book.save()

            self.stdout.write(self.style.SUCCESS(f'Import complete. Created {books_created} books.'))

        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(f'Error: Could not decode JSON from {json_file_path}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An unexpected error occurred: {e}'))
