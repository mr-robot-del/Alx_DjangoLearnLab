from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
    help = 'Sample queries for relationships'

    def handle(self, *args, **options):
        # Add sample data if none exists (run once in shell if needed)
        if not Author.objects.exists():
            author = Author.objects.create(name='J.K. Rowling')
            book = Book.objects.create(title='Harry Potter', author=author, publication_year=1997)
            library = Library.objects.create(name='Central Library')
            library.books.add(book)
            Librarian.objects.create(name='Jane Doe', library=library)

        # Query all books by a specific author
        author = Author.objects.get(name='J.K. Rowling')
        books_by_author = Book.objects.filter(author=author)
        self.stdout.write("Books by author: " + ", ".join([book.title for book in books_by_author]))

        # List all books in a library
        library = Library.objects.get(name='Central Library')
        books_in_library = library.books.all()
        self.stdout.write("Books in library: " + ", ".join([book.title for book in books_in_library]))

        # Retrieve the librarian for a library
        librarian = Librarian.objects.get(library=library)
        self.stdout.write("Librarian: " + librarian.name)
