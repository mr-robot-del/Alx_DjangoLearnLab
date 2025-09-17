# This setup is required to run the script standalone
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings') # Replace 'django-models' with your project's name
django.setup()

# Now you can import your models
from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Example data creation (optional, but helpful for testing)
    author1, _ = Author.objects.get_or_create(name='J.K. Rowling')
    book1, _ = Book.objects.get_or_create(title='The Sorcerer\'s Stone', author=author1)
    book2, _ = Book.objects.get_or_create(title='The Chamber of Secrets', author=author1)
    
    library1, _ = Library.objects.get_or_create(name='Downtown Library')
    library1.books.add(book1, book2)
    
    librarian1, _ = Librarian.objects.get_or_create(name='Mr. Smith', library=library1)

    print("--- Running Sample Queries ---")

    # 1. Query all books by a specific author
    print("\n1. Books by J.K. Rowling:")
    books_by_author = Book.objects.filter(author__name='J.K. Rowling')
    for book in books_by_author:
        print(f"- {book.title}")

    # 2. List all books in a library
    print("\n2. Books in Downtown Library:")
    library = Library.objects.get(name='Downtown Library')
    books_in_library = library.books.all()
    for book in books_in_library:
        print(f"- {book.title}")

    # 3. Retrieve the librarian for a library
    print("\n3. Librarian for Downtown Library:")
    librarian = Librarian.objects.get(library__name='Downtown Library')
    print(f"- {librarian.name}")

if __name__ == '__main__':
    run_queries()
