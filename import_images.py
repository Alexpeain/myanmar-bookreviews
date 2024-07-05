import csv
import os
from PIL import Image

csv_file = "./data/booknauthorimage.csv"  #temporary remove
book_data = []

with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row['Book Titles']
        author = row['Author']
        image_file = row['Covers']
        book_data.append({
            'title': title,
            'author': author,
            'image_file': image_file
        })

static_dir = 'static'
images_dir = os.path.join(static_dir, 'images')
covers_dir = os.path.join(images_dir, 'covers')

if not os.path.exists(covers_dir):
    os.makedirs(covers_dir)

for book in book_data:
    title = book['title']
    author = book['author']
    image_file = book['image_file']

    image_path = os.path.join(covers_dir, image_file)
    if os.path.exists(image_path):
        try:
            image = Image.open(image_path)
            image.save(image_path)  # Save the image to the same path
            print(f"Saved cover image for '{title}' by {author}")
        except (FileNotFoundError, OSError) as e:
            print(f"Error processing image file: {image_file}")
            print(e)
    else:
        print(f"No image found for '{title}' by {author}")