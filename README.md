# MyanBookReviews

> A backend-focused book review platform for avid readers in Myanmar. This project was built to learn and demonstrate core backend development skills, including API design, database management, and CI/CD.

![HomepageView](static/images/HomepageView.jpeg)

---

## ✨ Features

- **Book Management:** Full CRUD (Create, Read, Update, Delete) functionality for book metadata and categorization.
- **User Management:** Secure user registration, login (Authentication), and permission handling (Authorization).
- **Reviews & Ratings:** Users can write detailed reviews and give star ratings to books.
- **Search & Filtering:** A robust search system to find books by title, author, or category.

### Planned Features

- Social Features (following users, timelines)
- Recommendation Engine
- User Notifications

---

## 🛠️ Tech Stack

### Backend

- **Framework:** Django
- **Database:** PostgreSQL
- **API:** Django REST Framework (implied)
- **Containerization:** Docker & Docker Compose
- **Testing/CI/CD:** GitHub Actions (implied)

### Frontend

- Vanilla HTML, CSS, and JavaScript

---

## 🚀 Getting Started

The simplest and recommended way to run this project locally is by using Docker and Docker Compose.

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/myanbookreviews.git](https://github.com/your-username/myanbookreviews.git)
cd myanbookreviews
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```env
DJANGO_SECRET_KEY=your_secret_key
POSTGRES_DB=myanbookreviews_db
POSTGRES_USER=myanbookreviews_user
POSTGRES_PASSWORD=your_db_password
```

### 3. Build and Run the Containers

```bash
docker-compose up --build
```

```bash
docker compose exec web python manage.py migrate
```

```bash
docker compose exec web python manage.py createsuperuser
```

### 4. Access the Application

Open your web browser and navigate to `http://localhost:8000` to access the application.

### 5. Stopping the Application

To stop the application, run:

```bash
docker-compose down
```

---

## 📄 License

## This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
