from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected output: <Book: Book object (1)>
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Expected output: Nineteen Eighty-Four
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())
# Expected output: <QuerySet []>
