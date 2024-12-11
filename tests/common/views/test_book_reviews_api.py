from django.test import TestCase
import rest_framework.test as drf
from django.urls import reverse

from bookStore.accounts.models import AppUser, UserProfile
from bookStore.catalog.models import Genre, Author, Book


class BookstoreIntegrationTests(TestCase):
    def setUp(self):
        self.client = drf.APIClient()

        # Create a user and authenticate
        self.user = AppUser.objects.create_user(username='testuser', password='12admin34', email='test@example.com')
        self.client.force_authenticate(user=self.user)
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)

        # Create test data
        self.genre = Genre.objects.create(name="FictionTest")
        self.author = Author.objects.create(first_name="Author", last_name="Name")
        self.book = Book.objects.create(
            title="Test Book",
            description="Description of test book",
            price=10.99,
            isbn="1234567890123",
            author=self.author,
            genre=self.genre
        )

    def test_book_reviews_api(self):
        # Create a review

        response = self.client.post(reverse('book_reviews_api', args=[self.book.id]), data={
            'title': 'Amazing book!',
            'content': 'This is a wonderful read. Highly recommend!',
        },
         format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("Amazing book!", response.data['title'])
        self.assertIn("This is a wonderful read. Highly recommend!", response.data['content'])

        # Get all reviews for the book
        response = self.client.get(reverse('book_reviews_api', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
