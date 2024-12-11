from django.test import TestCase
from django.urls import reverse
from bookStore.catalog.models import Book, Genre, Author

class BookListViewTests(TestCase):

    def setUp(self):
        self.genre1 = Genre.objects.create(name="FictionTest")
        self.genre2 = Genre.objects.create(name="Non-Fiction")
        self.author1 = Author.objects.create(first_name="John", last_name="Doe")
        self.author2 = Author.objects.create(first_name="Jane", last_name="Smith")

        Book.objects.create(title="Book 1", genre=self.genre1, author=self.author1, price=15.99, isbn='0000000001')
        Book.objects.create(title="Book 2", genre=self.genre2, author=self.author2, price=25.99, isbn='0000000002')
        Book.objects.create(title="Another Book", genre=self.genre1, author=self.author2, price=20.00, isbn='0000000003' )

    def test_filter_by_genre(self):
        response = self.client.get(reverse('book_list'), {'genre': 'FictionTest'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['books']), 2)  # Only Fiction books
