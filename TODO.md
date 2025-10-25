# 📚 Book Review App — Improvement & Deployment Checklist

## 🚨 High Priority Tasks

- [x] Add a `slug` field to the `Book` model for SEO-friendly URLs
- [x] Fix slug generation for `Genre` and `Author` models
- [ ] Override `save()` method in `Book` to auto-generate slug
- [ ] Update `urls.py` to use `<slug:slug>` for book detail URLs
- [ ] Write a view to handle book detail by slug

### ⚙️ Automation

~~ - [ ] Automate pagination check for scraped book sites (e.g. cron job to detect new books daily) ~~

- [ ] using n8n for automation

---

## 🌱 Future Enhancements

- [ ] Implement user review system
- [ ] Add `Review` model with rating, text, and user fields
- [ ] Create review submission form on book detail page
- [ ] Add schema markup for reviews (for star ratings in search)
- [ ] Create admin interface for managing genres

---

## 🧹 Minor Fixes

- [ ] Add `alt` text to book cover images

---

## 👤 Authentication & User Profiles

- [ ] Use Django auth system for login/registration
- [ ] Create user profile pages showing reviews and info
- [ ] Add login/register buttons to navbar
- [ ] Consider `django-allauth` for social login support

---

## 🔍 Search Functionality

- [x] Ensure search returns relevant results
- [ ] Fix broken search buttons
- [x] Add search by author, genre, and book title

---

## ⭐ Rating System

- [ ] Allow users to rate books (1–5 stars)
- [ ] Enforce `unique_together = ('user', 'book')` in `Review`
- [ ] Add cached `average_rating` field on `Book` model
- [ ] Use signals to update rating on review save/delete

---

## 🎨 Frontend Improvements

- [ ] Improve homepage UI
- [ ] Add genre buttons to book detail page
- [ ] Enhance book list page UI
- [ ] Redesign genre page UI

---

## 🧭 SEO & Sitemap

- [ ] Generate SEO sitemap for Burmese book reviews
- [ ] Normalize Unicode and strip diacritics for slugs
- [ ] Evaluate slug libraries: `unidecode`, `pyicu`, or custom regex

---

## 🚀 Deployment Readiness

### ✅ Production-Like Testing

- [ ] Set up Gunicorn as WSGI server
- [ ] Configure Nginx as reverse proxy
- [ ] Simulate traffic with ApacheBench or Locust
- [ ] Verify static/media file serving
- [ ] Confirm Unicode rendering for Burmese text

### 🔡 Slug Generation Robustness

- [ ] Test with Burmese edge cases:
  - `ပြည်ထောင်စု`
  - `မြန်မာ့သမိုင်း`
  - `အတ္ထုပ္ပတ္တိ`

### 💬 Dynamic Content & Reviews

- [ ] Ensure Burmese reviews render correctly
- [ ] Protect review form from spam/XSS
- [ ] Add timestamps or avatars for trust signals

### 🧪 Test Suite Coverage

- [ ] Unit tests for slug generation
- [ ] Integration tests for login/signup and role-based access
- [ ] Use `pytest` or Django test runner with coverage reports

### 🚀 Staging Deployment

- [ ] Deploy to free-tier VPS (Render, Railway, Fly.io)
- [ ] Test slug URLs and Unicode rendering
- [ ] Monitor logs for encoding errors or 500s

### 🔐 Security Audit

- [ ] Change default `/admin` route
- [ ] Sanitize all user inputs
- [ ] Implement HTTPS and CSP headers
- [ ] Use `django-secure` or similar middleware

---

## 🧠 Performance & Scaling

### 🔒 Security Settings

- [ ] `CSRF_COOKIE_SECURE=True`
- [ ] `SESSION_COOKIE_SECURE=True`
- [ ] `SECURE_HSTS_SECONDS=31536000`
- [ ] `SECURE_REFERRER_POLICY='strict-origin-when-cross-origin'`
- [ ] Add `CONTENT_SECURITY_POLICY` header

### 🧮 Caching Strategy

- [ ] Cache book detail page (60–120s)
- [ ] Cache average ratings (5–10 min)
- [ ] Invalidate cache on review save/delete

### CORS Configuration

- [x] Install `django-cors-headers`
- [x] Add `corsheaders` to `INSTALLED_APPS`

### 🚦 Rate Limiting

- [ ] Limit to 5 reviews/user/hour
- [ ] Limit to 10 login attempts/IP/10 min
- [ ] Use `django-ratelimit`

### 🧰 Redis & Celery (When Needed)

- [ ] Install `django-redis` and configure `CACHES`
- [ ] Cache keys: `book:{id}:avg_rating`, `book:{id}:detail`
- [ ] Use signals to invalidate cache
- [ ] Add Celery for background tasks (emails, aggregates)

---

## 🧪 CI/CD Pipeline

- [ ] GitHub Actions: run tests + lint (`flake8` or `ruff`)
- [ ] Add build-and-deploy after Dockerfile is stable

---

## 🧠 Visual Debugging & Monitoring

- [ ] Add Django Debug Toolbar locally
- [ ] Add Sentry (free tier) for error tracking
- [ ] Optional: Prometheus/Grafana for metrics

---

## 🧭 UX Enhancements

- [ ] Add sort/filter by rating, recency, language, genre
- [ ] Watch [UX video](https://www.youtube.com/watch?v=Oi6XFdZW69A)

---

## 🧠 Developer Tips

- Draw data-flow diagram:  
  `User → Django View → ORM → DB → Cache → Template/JSON`
- Sequence diagrams for:
  - Create Review
  - Update Rating Aggregate

---

📚 How to Generate an SEO Sitemap in Django
To generate an SEO sitemap for your Burmese book reviews in Django, you can use Django's built-in sitemap framework. This is the most efficient and standard method. Here are the steps:

Enable the sitemaps framework:

Add 'django.contrib.sitemaps' to your INSTALLED_APPS in settings.py.

Also, ensure that 'django.contrib.sites' is in INSTALLED_APPS, as the sitemap framework depends on it.

Define your sitemap class:

Create a file (e.g., sitemaps.py) in your app.

Inside, create a Sitemap subclass. To handle book reviews, you would query the Book model.

Example Code:

# myapp/sitemaps.py

from django.contrib.sitemaps import Sitemap
from .models import Book

class BookSitemap(Sitemap):
changefreq = "weekly"
priority = 0.9

    def items(self):
        return Book.objects.all()

    def lastmod(self, obj):
        return obj.last_modified

Configure urls.py:

Import the sitemaps from your app and sitemap from Django.

Define a dictionary to map a name to your sitemap class.

Add a URL pattern to serve the sitemap.

Example Code:

# myproject/urls.py

from django.contrib.sitemaps.views import sitemap
from django.urls import path
from myapp.sitemaps import BookSitemap

sitemaps = {
'books': BookSitemap,
}

urlpatterns = [
path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

# ... other paths

]

Update your SITE_ID:

The sitemaps framework uses the SITE_ID from django.contrib.sites.

In settings.py, make sure you have SITE_ID = 1. You can then configure the domain name and other details in the Django admin under the "Sites" app.

Once these steps are complete, Django will generate a dynamic sitemap.xml file at the specified URL (/sitemap.xml in this example) that lists all your book review pages, which search engines like Google can crawl.
