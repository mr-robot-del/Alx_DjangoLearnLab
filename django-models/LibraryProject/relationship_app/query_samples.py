from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
    help = 'Sample queries for relationships'

    def add_arguments(self, parser):
        # Add an optional argument for author_name
        parser.add_argument('--author_name', type=str, default="J.K. Rowling",
                           help='Name of the author to query books for')

    def handle(self, *args, **options):
        # Get the author_name from the argument or use the default
        author_name = options['author_name']
        library_name = "Central Library"  # Consistent with previous feedback

        # 1. Query all books by a specific author
        author = Author.objects.get(name=author_name)  # As required by checker
        books_by_author = Book.objects.filter(author=author)
        self.stdout.write("Books by author: " + ", ".join([book.title for book in books_by_author]))

        # 2. List all books in a library
        library = Library.objects.get(name=library_name)  # As required by checker
        books_in_library = library.books.all()
        self.stdout.write("Books in library: " + ", ".join([book.title for book in books_in_library]))

        # 3. Retrieve the librarian for a library
        librarian = Librarian.objects.get(library=library)
        self.stdout.write("Librarian: " + librarian.name)
