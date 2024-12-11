from django.test import TestCase
from django.urls import reverse

from bookStore.catalog.models import Genre, Author, Book


class BookDetailsViewTests(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(name="FictionTest")
        self.author = Author.objects.create(first_name="Emily", last_name="Bronte")
        self.book = Book.objects.create(title="Wuthering Heights", genre=self.genre, author=self.author, price=18.99)

    def test_book_details_view(self):
        response = self.client.get(reverse('book_details', kwargs={'id': self.book.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['book'], self.book)