Admin Setup for Bookshelf App
    This document outlines the process of integrating and customizing the `Book` model in the Django admin interface for the `bookshelf` app.

    ## Step 1: Create a Superuser
    To access the admin interface, a superuser is required for login.
    ```bash
    python3 manage.py createsuperuser
    ```
    - Entered username (e.g., `admin`), email (optional), and password.
    - Output: `Superuser created successfully.`
    - Verification: Logged in at `http://localhost:8000/admin/` using the credentials.

    ## Step 2: Register and Customize the Book Model
    Modified `bookshelf/admin.py` to register the `Book` model with customizations for the admin interface.
    ```python
    from django.contrib import admin
    from .models import Book

    @admin.register(Book)
    class BookAdmin(admin.ModelAdmin):
        list_display = ['title', 'author', 'publication_year']
        list_filter = ['publication_year']
        search_fields = ['title', 'author']
    ```
    - `list_display`: Displays `title`, `author`, and `publication_year` in the list view.
    - `list_filter`: Adds a filter sidebar for `publication_year`.
    - `search_fields`: Enables searching by `title` or `author`.
    - Note: Removed duplicate `admin.site.register(Book)` to avoid `AlreadyRegistered` error.
    - Verification: Restarted the server (`python3 manage.py runserver 0.0.0.0:8000`). The “Books” section appeared at `/admin/bookshelf/book/`. Added books (e.g., “1984”, “George Orwell”, 1949), confirmed columns showed in the list view, filtered by year, and searched by title/author.

    ## Notes
    - The server runs with `0.0.0.0:8000` in Docker with port mapping (`-p 8000:8000`).
    - The admin interface is accessible at `http://localhost:8000/admin/` from the host browser.
    - Ensured `bookshelf` is in `INSTALLED_APPS` in `settings.py`.

