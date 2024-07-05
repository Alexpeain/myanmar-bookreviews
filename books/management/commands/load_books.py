from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from books.models import Book

class Command(BaseCommand):
    help = 'Scrapes book data from a website and saves it to the database'

    def handle(self, *args, **options):
        # URL of the website you want to scrape
        url = "https://www.pannsattlann.com/shop/"

        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the product listings
        product_listings = soup.find_all("li", class_="product")

        # Loop through each product listing and save the data to the database
        for listing in product_listings:
            # Get the book title
            title = listing.find("h2", class_="woocommerce-loop-product__title").text.strip()

            # Get the author name
            author = listing.find("a", class_="author-loop").text.strip()

            # Get the image URL
            image_url = listing.find("img", class_="attachment-woocommerce_thumbnail")["src"]

            # Create a new Book object and save it to the database
            book = Book(title=title, author=author, image_url=image_url)
            book.save()

        self.stdout.write(self.style.SUCCESS('Data has been saved to the database.'))