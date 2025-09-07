import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')  # Replace 'django_models' with your actual project name if different
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Step 1: Create sample data (run this once; comment out after to avoid duplicates)
def create_sample_data():
    # Create Authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="J.R.R. Tolkien")
    
    # Create Books with ForeignKey to Authors
    book1 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="The Hobbit", author=author2)
    
    # Create Libraries with ManyToMany to Books
    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book2)  # Add books to library
    
    library2 = Library.objects.create(name="University Library")
    library2.books.add(book2, book3)
    
    # Create Librarians with OneToOne to Libraries
    Librarian.objects.create(name="Alice Smith", library=library1)
    Librarian.objects.create(name="Bob Johnson", library=library2)

# Uncomment the line below to create data (run once)
# create_sample_data()

# Step 2: Sample Queries

# Query 1: All books by a specific author (ForeignKey example)
specific_author = Author.objects.get(name="J.K. Rowling")
books_by_author = Book.objects.filter(author=specific_author)
print("Books by J.K. Rowling:")
for book in books_by_author:
    print(book.title)

# Query 2: List all books in a library (ManyToMany example)
specific_library = Library.objects.get(name="Central Library")
books_in_library = specific_library.books.all()
print("\nBooks in Central Library:")
for book in books_in_library:
    print(book.title)

# Query 3: Retrieve the librarian for a library (OneToOne example)
librarian_for_library = specific_library.librarian
print("\nLibrarian for Central Library:")
print(librarian_for_library.name)
