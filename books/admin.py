from django.contrib import admin
from .models import Book,Review,Genre 
# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "display_genres","slug")
    # Because genres is manytomany 
    def display_genres(self, obj):
        """
        Creates a comma-separated string of genres for the list view.
        """
        return ", ".join([genre.name for genre in obj.genres.all()])

    display_genres.short_description = "Genres"

admin.site.register(Book, BookAdmin)
admin.site.register(Genre)