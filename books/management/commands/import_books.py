from books.models import Book
import csv
import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import books from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')
        
    def handle(self, *args, **options):
        # csv_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'booknauthorimg.csv')    
        csv_file = "./data/booknauthorimage.csv"
        with open(csv_file, 'r',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row['Book Titles']
                author = row['Author']
                cover = row['Covers']

                # Create or get the Book instance
                book, created = Book.objects.get_or_create(
                    title=title,
                    author=author,
                    cover=cover
                )

                # Add genres (assuming you have a Genre model)
                # You can add logic to handle genre mapping here
                # book.genres.add(genre1, genre2, ...)

                self.stdout.write(self.style.SUCCESS(f'Imported book: {title}'))