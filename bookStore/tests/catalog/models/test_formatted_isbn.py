from django.test import TestCase
from bookStore.catalog.models import Book, Author, Genre


class BookFormattedISBNTests(TestCase):

    def setUp(self):
        self.author = Author.objects.create(first_name="Emily", last_name="Bronte")
        self.genre = Genre.objects.create(name="Classic", description="Classic genre")

    def test_formatted_isbn_13(self):
        book = Book.objects.create(
            title="Wuthering Heights",
            isbn="9780316015844",
            author=self.author,
            genre=self.genre,
            price=15.00
        )
        self.assertEqual(book.formatted_isbn, "978-0-31-601584-4")

    def test_formatted_isbn_10(self):
        book = Book.objects.create(
            title="Jane Eyre",
            isbn="0316769487",
            author=self.author,
            genre=self.genre,
            price=15.00
        )
        self.assertEqual(book.formatted_isbn, "0-316-76948-7")
