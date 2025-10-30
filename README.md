# Personal BOOK&NOOK Project

<br> Myanmar BookReviews MyanBookReviews

### Description

### Purpose of the project

- Learn By Building Focus on Backend S
- For passion as an avid reader who does't have time and want to save time

### Set up the installations

set virtual environments

```
python -m venv .myenv
```

Activate the virtual environment

```source .myenv/bin/activate

```

Install the requirements

```pip install -r requirements.txt

```

### Docker

```
docker-compose up --build -d
```

### Migrate the database

```
docker-compose exec web python manage.py migrate

```

### Createsuperuser

```docker-compose exec web python manage.py createsuperuser

```

### Set the runserver

```docker-compose exec web python manage.py runserver 0.0.0.0:8001

```

#### Backend stacks and Configuration

- implement CRUD, API, Authetication & Authorization ,Web Security,
- Postgresql (DB scheme), logs, Performance (CICD)

#### Frontend Techology

- Javscript ,HTML,CSS

#### Business Logic

- Book Management (Add, Delete, edit)

  - Data Model handling Book Metadata
  - orgainze books into categories

- User Manangement

  - User registration /Authentication & Authorization
  - user -create account and manage (data ,editing /adding books)

- Reviews And Rating
  - enable user to write /rate books
- Searching and filetering

- Social Feature
- Recommendation (base on preference reaching histories)
- Notification

### Frontend Page View

![HomepageView](static/images/HomepageView.jpeg)

## License

[MIT License](LICENSE)
