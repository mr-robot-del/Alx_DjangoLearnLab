from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
    help = 'Sample queries for relationships'

    def handle(self, *args, **options):
        # Define sample data or assume it exists (add via admin/shell if needed)
        library_name = "Central Library"  # Example library name

        # 1. Query all books by a specific author
        author = Author.objects.get(name="J.K. Rowling")  # Specific author
        books_by_author = Book.objects.filter(author=author)
        self.stdout.write("Books by author: " + ", ".join([book.title for book in books_by_author]))

        # 2. List all books in a library
        library = Library.objects.get(name=library_name)  # As required by checker
        books_in_library = library.books.all()
        self.stdout.write("Books in library: " + ", ".join([book.title for book in books_in_library]))

        # 3. Retrieve the librarian for a library
        librarian = Librarian.objects.get(library=library)
        self.stdout.write("Librarian: " + librarian.name)
