# Basic API for Managing Books

## Overview

This project sets up a basic API for managing books, utilizing Django and Django REST Framework (DRF). The API provides an endpoint (`/api/books`) that allows listing and creating books, accessible through DRF’s browsable API interface. The interface, as shown in the image below, enables users to view a list of books and add new ones via a simple form.

![Book List Create API](<basic-API-for-managing-books.png>)
The image shows a "Book List Create API" with an endpoint (/api/books) that can list and create books using DRF’s (Django REST Framework) browsable API interface.

## Features

- **List Books**: Retrieve a list of all books with details like title, author, published date, and a calculated "days since published" field.
- **Create Books**: Add new books using the browsable API form.
- **Secure Configuration**: Uses a secure `SECRET_KEY` stored in a `.env` file and excludes sensitive files with `.gitignore`.
- **Extensible**: Supports additional fields (e.g., genre) and custom serializer logic.

## Prerequisites

- **Ubuntu WSL** (or any Linux-based system)
- **Python 3.6+**
- **pip** (Python package manager)
- **Git** (optional, for version control)

## Installation

### 1. Clone the Repository

If using Git, clone the project:

```bash
git clone https://github.com/BunnyeNyash/book_management.git
cd book_management
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install django djangorestframework python-dotenv
```

### 4. Configure Environment Variables

1. Create a .env file in the project root (~/book_management):

```bash
vi .env
```

2. Add a secure SECRET_KEY (generate one with the command below) and other settings:

```
SECRET_KEY='your-secure-key-here'
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
```

- Generate a secure key:

```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

3. Save and exit the .env file using ESC then :wq

### 5. Apply Migrations

Set up the database:

```bash
python3 manage.py migrate
```

### 6. Run the Development Server

Start the server to test the API:

```bash
python3 manage.py runserver
```

- Visit http://127.0.0.1:8000/api/books/ in your browser to see the browsable API.

## Project Structure
```
book_management/
├── book_management/ # Project configuration
│ ├── **init**.py
│ ├── settings.py # Configuration (e.g., SECRET_KEY, ALLOWED_HOSTS)
│ ├── urls.py # URL routing
│ ├── wsgi.py # WSGI deployment
│ └── asgi.py # ASGI deployment
├── book_app/ # App for book management
│ ├── migrations/ # Database migration files
│ ├── **init**.py
│ ├── models.py # Defines the Book model
│ ├── serializers.py # Handles data serialization
│ ├── views.py # Defines the BookViewSet
│ └── urls.py # URL configuration for the API
├── manage.py # Management command-line utility
├── .env # Environment variables (e.g., SECRET_KEY)
├── .gitignore # Excludes sensitive files from Git
└── README.md # This file
```

## Configuration

- .env: Stores sensitive data like SECRET_KEY, DEBUG, and ALLOWED_HOSTS. Ensure .env is listed in .gitignore.
- settings.py: Loads .env variables and sets DEBUG and ALLOWED_HOSTS. Update ALLOWED_HOSTS for production domains.
- .gitignore: Prevents tracking of venv/, db.sqlite3, .env, and other local files.

## Development Notes

- Debug Mode: Set DEBUG = True in settings.py for detailed error pages during development, but use DEBUG = False with ALLOWED_HOSTS set for production.
- Testing: Use the browsable API at /api/books/ or tools like Postman for API testing.
