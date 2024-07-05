from django.contrib import admin
from .models import Book,Review,Genre 
# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "Bid")


admin.site.register(Book, BookAdmin)
admin.site.register(Genre)