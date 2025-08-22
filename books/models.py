from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import os
from django.core.files import File
from urllib.request import urlopen
from django.utils.text import slugify
from unidecode import unidecode




import uuid
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    Bid = models.UUIDField( primary_key=True,default=uuid.uuid4,editable=False)
    #id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    # add slug field for SEO-friendly URLs
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.CharField(max_length=200)
    # description = models.TextField(null=True,blank=True)
    description = models.TextField(default='')
    cover = models.URLField(blank=True, null=True)
    genres = models.ManyToManyField(Genre,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.create_slug(self.title)
        super().save(*args, **kwargs)

    def create_slug(self, title):
        # Convert the title to ASCII
        ascii_title = unidecode(title)
        # Generate a slug from the ASCII title
        slug = slugify(ascii_title)
        return slug

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # new
        return reverse("book_detail", args=[str(self.Bid)])
    class Meta:
        indexes = [ # new
        models.Index(fields=["Bid"], name="id_index"),]

        
class Review(models.Model):
    book = models.ForeignKey(Book,
            on_delete=models.CASCADE,
            related_name="reviews",
        )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)

