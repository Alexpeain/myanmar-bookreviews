# App Improvement Tasks

## High Priority

- [ ] Add a `slug` field to the `Book` model for SEO-friendly URLs.
- [ ] Override the `save()` method in the `Book` model to automatically generate the slug.
- [ ] Update `urls.py` to use `<slug:slug>` for book details.
- [ ] Write a view to handle the new book detail URL.

#### for Automation

- [ ] automate check if the scraped books website has been updated their pagination and scrape the new books. eg run a cron job to check for new books every day.

## Future Enhancements

- [ ] Implement a user review system for books.
- [ ] Add a `Review` model with fields for rating, text, and user.
- [ ] Create a form for submitting reviews on the book detail page.
- [ ] Add schema markup for reviews to show star ratings in search results.
- [ ] Create an admin page for managing book genres.

## Minor Fixes

- [ ] Add `alt` text to book cover images.
