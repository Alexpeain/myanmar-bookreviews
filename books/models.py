from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
import uuid
import unicodedata
import re

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

def build_myanmar_slug(title: str) -> str:
    # Normalize Unicode so Myanmar diacritics combine properly
    t = unicodedata.normalize("NFC", title).strip()

    # Split words by whitespace
    parts = re.split(r"\s+", t)

    # Join all parts with a "+" sign as the slug
    if not parts:
        return ""
    slug = "+".join(parts)

    #  replace characters you don’t want in slugs.
    slug = slug.replace("/", "-")

    return slug

class Book(models.Model):
    Bid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, allow_unicode=True, null=True)
    author = models.CharField(max_length=200)
    description = models.TextField(default='')
    cover = models.URLField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    title_searchable = models.CharField(max_length=255, editable=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Build a custom Unicode slug that preserves Myanmar text and uses +
            base_slug = build_myanmar_slug(self.title)

            # Fallback to django slugify if base_slug ends empty
            if not base_slug:
                base_slug = slugify(self.title, allow_unicode=True)

            # Ensure uniqueness
            slug_candidate = base_slug
            counter = 1
            while Book.objects.filter(slug=slug_candidate).exists():
                slug_candidate = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug_candidate

        self.title_searchable = re.sub(r"\s+", "", self.title).lower()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Want URLs like /books/book/<slug>
        return reverse("book_detail", args=[self.slug])

    class Meta:
        indexes = [] # Removed the redundant index on Bid
        ordering = ['title']

class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        preview = (self.review[:50] + "...") if len(self.review) > 50 else self.review
        return f"{self.book.title}: {preview}"
