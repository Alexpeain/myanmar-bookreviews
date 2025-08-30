# App Improvement Tasks

## High Priority

- [ ] Add a `slug` field to the `Book` model for SEO-friendly URLs.
- [] fix slug for genres and author too
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

### Add Authentication and User Profiles login and registration Buttons

- [ ] Implement user authentication using Django's built-in auth system.
- [ ] Create user profile pages to display user information and their reviews.
- [ ] Add login and registration buttons to the navigation bar.

### Fixed Search Functionality

- [ ] Ensure the search functionality works correctly and returns relevant results.

### Rating system

- [ ] Implement a rating system for books, allowing users to rate books from 1 to 5 stars.

### Deployment

### Testing and Documentation

### Frontend Improvements

- [] home page UI
- [] book detail page UI button for genres
- [] book list page UI
- [] genre page UI

### Search Fields

- [] add search by author and genre and book title

how to generate an SEO sitemap for all your Burmese book reviews in Django?
