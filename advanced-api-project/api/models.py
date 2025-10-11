from django.db import models

# model representing an author of books.
# purpose: Stores Basic author information and links to their books via one to many relationship.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model representing book written by an author
# Purpose: stores books details and establishes a foreign key relationship to Author
# The relationship allows querying books by authors (e.g., author.books.all())
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    def __str__(self):
        return f"{self.title} by {self.author.name}"
