from bookStore.catalog.models import Author, Book, Genre
from django.test import TestCase


class AuthorTotalBooksTests(TestCase):

    def setUp(self):
        self.author = Author.objects.create(first_name="Jane", last_name="Smith")
        self.genre = Genre.objects.create(name="Fiction", description="Fictional genre")

    def test_total_books(self):
        Book.objects.create(title="Book 1", isbn="1234567890", author=self.author, genre=self.genre, price=19.99)
        Book.objects.create(title="Book 2", isbn="1234567890123", author=self.author, genre=self.genre, price=29.99)
        self.assertEqual(self.author.total_books, 2)