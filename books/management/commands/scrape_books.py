import requests
from bs4 import BeautifulSoup
import time
import random
import os
import urllib.request # To download images

# Import Django components
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File # To wrap downloaded image data
from django.core.files.temp import NamedTemporaryFile # To save temporary image file

# Import your Book model
from your_app_name.models import Book # Replace 'your_app_name' with the actual name of your Django app

# --- Scraping Configuration ---
BASE_SHOP_URL = 'https://www.pannsattlann.com/shop/'
TOTAL_PAGES = 76 # Based on website structure
# Note: It's better to dynamically find the total pages as discussed before

# --- Scraping Logic (adapted) ---

def scrape_single_page_books(url):
    """
    Scrapes book titles, image URLs, and authors from a single shop page.
    Does NOT save to DB here, just returns the data.

    Args:
        url (str): The URL of the shop page.

    Returns:
        list: A list of dictionaries, each containing data for a book,
              or None if the page could not be fetched due to an error.
    """
    try:
        headers = {
            'User-Agent': 'YourBookReviewsAppScraper/1.0 (+http://your-app-website.com - Management Command)' # Be descriptive
        }

        # Introduce a random delay before the request
        delay = random.uniform(5, 10)
        print(f"Waiting {delay:.2f} seconds before requesting {url}")
        time.sleep(delay)

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        books_data_on_page = [] # Use a different name to avoid confusion with the main list
        product_items = soup.select('li.product')

        if not product_items:
            print(f"No product items found on {url}. Check selectors or page content.")
            return []

        for i, item in enumerate(product_items):
            book_info = {}
            try:
                title_element = item.select_one('h2.woocommerce-loop-product__title')
                book_info['title'] = title_element.text.strip() if title_element else 'N/A'

                image_element = item.select_one('img.lazyload')
                # Prefer data-original, fallback to src
                image_url = image_element.get('data-original') if image_element else 'N/A'
                if image_url == 'N/A' and image_element:
                     image_url = image_element.get('src', 'N/A')

                book_info['image_url'] = image_url

                author_element = item.select_one('a.author-loop')
                book_info['author'] = author_element.text.strip() if author_element else 'N/A'

                books_data_on_page.append(book_info)

            except Exception as e:
                print(f"Error extracting data for item {i+1} on {url}: {e}")
                continue

        print(f"Successfully scraped {len(books_data_on_page)} books data from {url}")
        return books_data_on_page

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {url}: {e}")
        return None


# --- Django Management Command ---

class Command(BaseCommand):
    help = 'Scrapes book data from Pann Satt Lann Books and saves to the Django database.'

    # Optional: Add arguments to control scraping behavior (e.g., number of pages)
    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         '--pages', type=int, default=TOTAL_PAGES, help='Number of pages to scrape'
    #     )

    def handle(self, *args, **options):
        # total_pages_to_scrape = options['pages'] # If you added the --pages argument

        self.stdout.write(f"Starting scraping process for all {TOTAL_PAGES} pages of {BASE_SHOP_URL}...")

        # Connect to the database is handled by Django's ORM automatically
        # We just need to interact with models

        for page_num in range(1, TOTAL_PAGES + 1):
            if page_num == 1:
                page_url = BASE_SHOP_URL
            else:
                page_url = f"{BASE_SHOP_URL}page/{page_num}/"

            self.stdout.write(f"\n--- Scraping page {page_num} of {TOTAL_PAGES} ---")
            page_data = scrape_single_page_books(page_url)

            if page_data is not None:
                self.stdout.write(f"Processing {len(page_data)} books from page {page_num}...")
                for book_info in page_data:
                    # --- Save book data to the database using Django ORM ---
                    try:
                        # Use get_or_create to avoid creating duplicate books
                        # based on title and author. If a book with the same title
                        # and author exists, it will return the existing book object.
                        book_obj, created = Book.objects.get_or_create(
                            title=book_info.get('title', 'Unknown Title'),
                            author=book_info.get('author', 'Unknown Author'),
                            defaults={} # Default values for creation if the object doesn't exist
                            # You could add description='', etc. here if you were scraping description too
                        )

                        if created:
                            self.stdout.write(self.style.SUCCESS(f"Created new book: {book_obj.title} by {book_obj.author}"))
                            # If it's a new book, attempt to download and save the image
                            image_url = book_info.get('image_url')
                            if image_url and image_url != 'N/A':
                                try:
                                    img_temp = NamedTemporaryFile(delete=True)
                                    img_temp.write(requests.get(image_url, stream=True).content)
                                    img_temp.flush()

                                    # Get the image file name from the URL
                                    image_name = image_url.split('/')[-1]
                                    # You might want to clean up the filename or add a timestamp
                                    # For example, replace spaces or special characters

                                    book_obj.cover.save(image_name, File(img_temp))
                                    self.stdout.write(f"Downloaded and saved cover for {book_obj.title}")
                                except Exception as img_e:
                                    self.stdout.write(self.style.WARNING(f"Could not download or save image for {book_obj.title}: {img_e}"))

                        else:
                            # Optional: Handle existing books (e.g., update description if you were scraping it)
                            # self.stdout.write(f"Book already exists: {book_obj.title}")
                             pass # Do nothing if the book already exists

                    except Exception as db_e:
                        self.stdout.write(self.style.ERROR(f"Error saving book {book_info.get('title', 'N/A')} to DB: {db_e}"))
                        # Decide how to handle DB errors - log, skip, retry?

            else:
                self.stdout.write(self.style.WARNING(f"Could not scrape page {page_num}. Skipping database insertion for this page."))

        self.stdout.write(self.style.SUCCESS('\nScraping and database saving process finished.'))