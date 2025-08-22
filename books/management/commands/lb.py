from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from books.models import Book
import time # Import time for delays
import random # Import random for varied delays

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Add headers to mimic a browser visit
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        # Start with the first page
        page_num = 1
        scraped_count = 0
        target_count = 100  # Your target number of books
        book_data = []  # Initialize book_data to track all books considered

        # Check Robots.txt for scraping permissions
        robots_url = "https://www.pannsattlann.com/robots.txt"
        try:    
            robots_response = requests.get(robots_url, headers=headers)
            robots_response.raise_for_status()
            if "Disallow: /shop/" in robots_response.text:
                self.stdout.write(self.style.ERROR("Scraping this site is not allowed according to robots.txt."))
                return
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Error fetching robots.txt: {e}"))
            return  
        
        while scraped_count < target_count:
            if page_num == 1:
                url = "https://www.pannsattlann.com/shop/"
            else:
                url = f"https://www.pannsattlann.com/shop/page/{page_num}/"

            self.stdout.write(f"Scraping page: {url}")

            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()

                soup = BeautifulSoup(response.content, "html.parser")
                product_listings = soup.find_all("li", class_="product")

                if not product_listings:
                    self.stdout.write(self.style.WARNING(f"No product listings found on page {page_num}. Ending scrape."))
                    break

                for listing in product_listings:
                    if scraped_count >= target_count:
                        break

                    try:
                        title_tag = listing.find("h2", class_="woocommerce-loop-product__title")
                        title = title_tag.text.strip() if title_tag else 'N/A'

                        author_tag = listing.find("a", class_="author-loop")
                        author = author_tag.text.strip() if author_tag else 'N/A'

                        img_tag = listing.find("img", class_="lazyload")
                        image_url = img_tag.get('data-original') or img_tag.get('src') if img_tag else None

                        if not title or title == 'N/A':
                            self.stdout.write(self.style.WARNING(f"Skipping a product due to missing title."))
                            continue

                        # Append to book_data
                        book_data.append({
                            "title": title,
                            "author": author,
                            "image_url": image_url
                        })

                        if not Book.objects.filter(title=title, author=author).exists():
                            book = Book(title=title, author=author, cover=image_url)
                            book.full_clean()
                            book.save()
                            scraped_count += 1
                            self.stdout.write(self.style.SUCCESS(f"Saved ({scraped_count}/{target_count}): {title} by {author}"))
                        else:
                            self.stdout.write(self.style.WARNING(f"Skipped duplicate: {title} by {author}"))

                    except AttributeError as e:
                        self.stdout.write(self.style.WARNING(f"Skipping a product due to missing data: {e} in listing: {listing}"))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"An unexpected error occurred processing a listing: {e}"))

                page_num += 1
                time.sleep(random.uniform(1, 3))

            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f"Error fetching page {page_num}: {e}"))
                break
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"An unexpected error occurred scraping page {page_num}: {e}"))
                break

        # Final success message
        self.stdout.write(self.style.SUCCESS(
            f'Scraping finished. Total books considered: {len(book_data)}. '
            f'Saved to database: {Book.objects.count()} (if running this command multiple times, count might be higher due to previous runs).'
        ))